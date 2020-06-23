console.log("Sanity check!");

// Class to hold basic item data (front-end)
class Item {
    constructor(id, itemId, description, price, discount=0, discountType=1, quantity=1){
        this.id = id;
        this.itemId = itemId;
        this.description = description;
        this.quantity = quantity;
        this.price = price;         // regular price 
        this.discount = discount;
        this.discountType = 1;       // 1: percentage off regular price; 2: ammount off, e.g., 50 cents
        this.specialDiscount = 0;   // this can manager's account, item damaged discount. etc
        this.discountCalc = 0;      // 
        this.purchasePrice = 0 ;    // this is the price to pay for the item. It is equal to (regular_price - discounts)
        this.comment ='';
    }
}
 
// Class to hold all transaction data
class TransactionData {
    constructor() {
        this.allItems = [];      // Array of Items
        this.totals = {
            price: 0,
            quantity: 0 
        }
        this.comment = '';
    }

    addItem(itemId, description, price, discount=0, discountType=1, quantity=1) {
        let id, newItem; 

        // Create new ID
        if (this.allItems.length > 0) {
            id = this.allItems[this.allItems.length - 1].id + 1;
        } else {
            id = 0;
        }

        newItem = new Item(id, itemId, description, price, discount=0, discountType=1, quantity=1); 
        this.allItems.push(newItem);  
        
        return newItem;
    }

    deleteItem(id) {
        // id = 6
        //data.allItems[id];
        // ids = [1 2 4 6 8]
        //index = 3
        
        let ids = this.allItems.map(item => item.id)
        let index = ids.indexOf(id);

        if (index !== -1) {
            this.allItems.splice(index, 1);
        }
    }

    // Reset transactionData to empty (ready for next transaction)
    resetData() {
        this.allItems.splice(0, this.allItems.length);
        this.totals.price = 0;
        this.totals.quantity = 0;
        this.comment = '';
    } 
    
} 

// Class to hold UI data and methods
class UIController {

    static #DOMstrings = {
        barcodeInput: 'barcode',
        itemsContainer: 'ItemsContainer',
        itemsList: 'items__list',
        transactionItem: '.transaction-item',
    };

    // Add and display the item in the allItems list
    static addListItem(item) {      
        // Create HTML string        
        let html = `<tr class="transaction-item" id="item-${item.id}">
          <td>${item.description}</td>
          <td>${item.quantity}</td>
          <td class='text-right'>${item.price}</td>
        </tr>`
        console.log(html);
        
        // Insert the HTML into the DOM
        const listRef = document.getElementById(this.#DOMstrings.itemsList);
        const newRow = listRef.insertRow();   // Insert a row at the end of the table
        newRow.innerHTML = html;
    }   
    
    // Delete the select item from UI display
    static deleteListItem(selectorID) {            
        const el = document.getElementById(selectorID);
        el.parentNode.removeChild(el);       
    }
        
    // Delelet all list items - empty the list for next transaction.
    static deleteAllListItems() {
        const listRef = document.getElementById(this.#DOMstrings.itemsList);
        while (listRef.firstChild) {
            listRef.removeChild(listRef.firstChild);
        }
    }

    // Reset the barcode input field.    
    static clearBarcodeField() {
        let el_barcode = document.getElementById(this.#DOMstrings.barcodeInput);
        el_barcode.value = '';
        el_barcode.focus();
    }

    // Reset UI display to ready for a new transaction
    static resetUI() {
        this.deleteAllListItems();
        this.clearBarcodeField();
    }
}


// Global variable to hold all transaction data
const transData = new TransactionData(); 

async function getItem(barcode) {
    try {
        const result = await fetch(`get_item/?barcode=${barcode}`);
        const data = await result.json();
        console.log(data);
        if(data.validInd === 1) {
            
            // 1. Add the item data to TransData
            const newItem = transData.addItem(data.itemId, data.description, data.price);
            console.log(newItem);
            console.log(transData);       

            // 2. add the item to UI display
            UIController.addListItem(newItem);

            // 3. Reset the barcode input box
            UIController.clearBarcodeField();

        } else {
            console.log("data not valid.")
        }

    } catch(error) {
        console.log(error);
    }
}

function getItemByCode() {
    const barcode =  document.getElementById('barcode').value;
    if (barcode.length > 0) {
      getItem(barcode);
    }
}

const setupEventListeners = () => {
    // When the Enter button is pressed
    document.getElementById('btn_enter').addEventListener('click', getItemByCode);

    // When a Enter key is pressed in Barcode input box
    document.getElementById('barcode').addEventListener('keypress', function(event) {   
        if((event.keyCode === 13) || (event.which === 13)) {
        event.preventDefault();
        getItemByCode();
        // console.log(event.target);
        // console.log(event.target, event.target.parentNode);
        // console.log(event.keyCode);
        }
    })

    // When the Send Data! button is clicked
    document.getElementById('send_trans_data').addEventListener('click', postTransData);

    document.getElementById('new_transaction').addEventListener('click', startNewTransaction);

}
setupEventListeners();


// Start a new transaction - discard previous data
function startNewTransaction() {
    // 1. Reset the transaction data to empty
    transData.resetData();

    // 2. remove previous items (if any) from UI
    UIController.resetUI(); 
}


// Send the transData to Server
function postTransData() {
        
    const URL_POST = 'transdata/';
    
    // Check data - rule out no transaction data.
    if (transData.allItems.length === 0) { 
        return 
    }
    console.log("sending transData...")

    const resp_json = postData(URL_POST, transData);
    console.log(resp_json);
}

// Post transactionn data to server after payment is done 
// data: should be an object of (k,v)'s 
async function postData(url, data) {

    const rawResponse = await fetch(url, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    const resp = await rawResponse.json();

    console.log(resp);
};