
		// var orderNo;
		function if_checked() {
			var counter = 0;

			for (var i = 0; i < (itemsform.length)-1; i++) {
				if(document.itemsform.elements[i].checked){
					counter++;
				}
			}
			try{
			if(counter==0) throw " no item selected please"; 
			}
			catch(err){
				alert(err);
			}
			
		}
		function mysearch(id,tablename,searchfield){
			var input,filter,table,tr,td,i;

			input= document.getElementById(id);
			filter= input.value.toUpperCase();
			table= document.getElementById(tablename);
			tr=table.getElementsByTagName("tr");

			for(i=0;i<tr.length;i++){
				td= tr[i].getElementsByTagName("td")[searchfield];
				if (td) {
					if (td.innerHTML.toUpperCase().indexOf(filter)> -1) {
						tr[i].style.display="";
					} else {
						tr[i].style.display= "none";
				}
			}

		}
		}

		function getOrder(Id) {
			var rowNo = document.getElementById(Id);
			var td = rowNo.getElementsByTagName("td")[0];

			alert(td.innerHTML); 
		}
		function setorder() {
			var order= document.getElementById("orderkey");
			 // orderNo=order.value;
		}

		function set_time() {
			var now = new Date();
			var hour_input = document.getElementById("hour");
			var min_input = document.getElementById("minute");
			var sec_input = document.getElementById("sec");

			hour_input.value=now.getHours();
			min_input.value= now.getMinutes();
			sec_input.value=now.getSeconds();
		}
		 setInterval("set_time()",1000);

		 function AutoRefresh( t ) {
           setTimeout("location.reload(true);", t);
}

