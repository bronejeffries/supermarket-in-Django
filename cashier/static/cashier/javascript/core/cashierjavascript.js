function clickExpenses(){

  document.getElementById('expiry-date').style.display='none';
  document.getElementById('Expiry').style.display='none';
  document.getElementById('amount-expense').style.display='block'; document.getElementById('amount').style.display='block';

}

function clickExpiry(){
  document.getElementById('amount-expense').style.display='none';
  document.getElementById('amount').style.display='none';
  document.getElementById('Expiry').style.display='block';
  document.getElementById('expiry-date').style.display='block';
}



function mysearch(id,tablename,searchfield){

  var input,filter,table,tr,td,i;

  input= document.getElementById(id);
  filter= input.value.toUpperCase();
  table= document.getElementById(tablename);
  tr=table.getElementsByTagName("tr");

  for(i=0;i<tr.length;i++){
    td = tr[i].getElementsByTagName("td")[searchfield];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter)> -1) {
        tr[i].style.display="";
      } else {
        tr[i].style.display= "none";
    }
  }

}
}




var table_list = document.getElementById('items_table');
var mylist = table_list.getElementsByTagName("tr");
var i;
for (i = 0; i < mylist.length; i++) {
  // var span = document.createElement("SPAN");
  // var txt = document.createTextNode("\u00D7");
  // span.className = "close";
  // span.appendChild(txt);
  // myNodelist[i].appendChild(span);

  var createClickHandler = function(row)
              {
                  return function() {
                    var selected_column = row.getElementsByTagName('td');
                    var table = document.getElementById('sales_table');

                      var tr = table.insertRow((table.getElementsByTagName('tr').length));
                      var td = document.createElement("td");

                      var id =  tr.insertCell(0);

                    var  Name = tr.insertCell(1);

                    var price = tr.insertCell(2);

                      var quantity = tr.insertCell(3);

                      var total = tr.insertCell(4);
                      total.className = "text-success";

                      id.innerHTML=(table.getElementsByTagName('tr').length) - 1;


                      Name.innerHTML= '<input  type="text" name="item" class="">';
                      Name.getElementsByTagName('input')[0].value = (selected_column[1].innerHTML).toString();
                      price.innerHTML = selected_column[2].innerHTML;
                      quantity.innerHTML='<input type="number" name="quantity" id='+"item"+id.innerHTML +' class="form-control  col-lg-5">';
                      total.innerHTML='<input type="number" name="total" class="form-control  col-lg-5">';
                      setInterval(function () {

                        total.getElementsByTagName('input')[0].value=(price.innerHTML)*(quantity.getElementsByTagName('input')[0].value);
                        console.log(total.innerHTML);
                      },100);

                                   };
              }

          mylist[i].onclick = createClickHandler(mylist[i]);

}

function findTot() {
  var sales_table = document.getElementById('sales_table');
  var rows = sales_table.getElementsByTagName('tr');
  var total_sales_btn = document.getElementById('sales_total');
  var total = 0;
  for (var i = 1; i < rows.length; i++) {
    var value = rows[i].getElementsByTagName('td')[4].getElementsByTagName('input')[0].value;
    total += Number(value);
  }
  if(total > 0){
      total_sales_btn.innerHTML = total + 'UGX';
  }else if (total== 0) {
    total_sales_btn.innerHTML='000UGX';
  }

}

setInterval('findTot()',10);

function add_to_reciept(id) {
  var  total_amount_btn = document.getElementById('reciept_total');

       var  reciepttotal = 0;

    var reciept_column = id.parentElement.parentElement.getElementsByTagName('td');

    var reciept_table = document.getElementById('reciept_view');

    var rows = reciept_table.getElementsByTagName('tr');

    var tr = reciept_table.insertRow(rows.length);
    // var td = document.createElement("td");


  var  item_name = tr.insertCell(0);

  var costprice = tr.insertCell(1);

    var quantity = tr.insertCell(2);

    var total = tr.insertCell(3);
    total.className = "text-primary";

    var item_name_value = reciept_column[0].getElementsByTagName('input')[0].value;
    var costprice_value = reciept_column[1].getElementsByTagName('input')[0].value;
    var quantity_value = reciept_column[2].getElementsByTagName('input')[0].value;


    item_name.innerHTML= '<input type="text" name="item_name" value='+ item_name_value +' class="form-control no-border">';
    costprice.innerHTML = '<input type="text" name="item_cost_price" value=' + costprice_value +' class="form-control no-border" >';
    quantity.innerHTML='<input type="text" name="item_quantity" value=' + quantity_value +' class="form-control no-border" >';

    // cost = costprice.getElementsByTagName('input')[0].value;
    // quantity_value = quantity.getElementsByTagName('input')[0].value;
    total.innerHTML=(costprice_value*quantity_value);

for (var i = 1; i < rows.length; i++) {
    var cells = rows[i].getElementsByTagName('td')[3];
    console.log(cells.innerHTML);
    reciepttotal += Number(cells.innerHTML);
}


        console.log(reciepttotal);
        total_amount_btn.innerHTML = reciepttotal;
}

function showupload(){
  document.getElementById('upload-invisible').style.display="block";
}

//  setInterval(function () {
//    var reciept_table = document.getElementById('reciept_view');
//    // var total_amount_btn = document.getElementById('reciept_total');
//    var reciept_rows = reciept_table.getElementsByTagName('tr');
//      // var reciepttotal = 0;
//      for (var i = 0; i < reciept_rows.length; i++) {
//        reciepttotal += Number(reciept_rows[i].getElementsByTagName('td')[3].innerHTML);
//      }
//      console.log('good');
//    total_amount_btn.innerHTML = reciepttotal;
//
// }, 10);
