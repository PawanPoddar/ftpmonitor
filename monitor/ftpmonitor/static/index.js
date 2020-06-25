
window.onload=initAll;
var buttonId;
function initAll(){
}
//function register()
//{
//var first=document.getElementByName('firstname').value;
//var last=document.getElementByName('lastname').value;
//var user=document.getElementByName('username').value;
//var pass=document.getElementByName('password').value;
//var repass=document.getElementByName('repassword').value;
//var email=document.getElementByName('email').value;
//var req=new XMLHttpRequest();
//var url='register?firstname='+first+'&lastname='+last+'&username='+user+'&password='+pass+'&repassword='+repass+'&email='+email;
//req.onreadystatechange = function() {
//    if (this.readyState == 4 && this.status == 200) {
////     document.getElementById("demo").innerHTML = this.responseText;
//    }
//  };
// req.open('POST',url,true);
// req.send();
//}

//var myVar = setInterval("realDetail();",1000);
function folderDetail()
{
//    clearInterval(myVar);
    var fo_name=document.getElementById('folderName').value;
    var req= new XMLHttpRequest();
    var url='allabout?f_name='+fo_name;
    req.onreadystatechange=function(){
        if(this.readyState == 4 && this.status == 200){
//        alert(req.responseText);
        var obj=req.responseText;
        var h= JSON.parse(obj)
        var all=h['data']
//        alert(all[0].name);
        var div=document.getElementById('abcd');
        div.innerHTML="";

        var table= document.createElement('TABLE');

        var row=table.insertRow(0);
            var name=row.insertCell(0);
            var date=row.insertCell(1);
            var time=row.insertCell(2);
            var status=row.insertCell(3);
            var check=row.insertCell(4);
            var size=row.insertCell(5);

            name.innerHTML ="FILE NAME";
            date.innerHTML="DATE ";
            time.innerHTML=" TIME ";
            status.innerHTML="STATUS";
            check.innerHTML="CHECK";
            size.innerHTML="SIZE"

        for (var i=0; i< all.length;i++)
        {
            var row=table.insertRow(i+1);
            var name=row.insertCell(0);
            var date=row.insertCell(1);
            var time=row.insertCell(2);
            var status=row.insertCell(3);
            var check=row.insertCell(4);
            var size=row.insertCell(5);

            name.innerHTML =all[i].name;
            date.innerHTML=all[i].date;
            time.innerHTML=all[i].time;
            status.innerHTML=all[i].status;
            check.innerHTML=all[i].check;
            size.innerHTML=all[i].size+" bytes";


        }
        table.className='table text-center table-hover'
        div.appendChild(table);

        }
    };
    req.open("GET",url,true);
    req.send();
}
//setInterval("realDetail();",1000);

function realDetail()
{
    var fo_name=document.getElementById('realName').value;
    var req= new XMLHttpRequest();
    var url='realTime?f_name='+fo_name;
    req.onreadystatechange=function(){
        if(this.readyState == 4 && this.status == 200){
//        alert(req.responseText);
        var obj=req.responseText;
        var h= JSON.parse(obj)
        var all=h['data']

        var div=document.getElementById('abcd');
        div.innerHTML="";
        var table= document.createElement('TABLE');
        var row=table.insertRow(0);
            var name=row.insertCell(0);
            var path=row.insertCell(1);
            var time=row.insertCell(2);
            var size=row.insertCell(3);

            name.innerHTML ="FILE NAME";
            path.innerHTML="FOLDER";
            time.innerHTML="DATE";
             size.innerHTML="SIZE"

        for (var i=0; i< all.length;i++)
        {
            var row=table.insertRow(i+1);
            var name=row.insertCell(0);
            var path=row.insertCell(1);
            var time=row.insertCell(2);
            var size=row.insertCell(3);

            name.innerHTML =all[i].name;
            path.innerHTML=all[i].path;
            time.innerHTML=all[i].time;
            size.innerHTML=all[i].size+" bytes";
        }
        table.className='table text-center table-hover'
        div.appendChild(table);
        }
    };
    req.open("GET",url,true);
    req.send();
}
function fileSearch()
{
    var file_name=document.getElementById('fileDetail').value;
    var req= new XMLHttpRequest();
    var url='fileSearch?file_name='+file_name;
    req.onreadystatechange=function(){
        if(this.readyState == 4 && this.status == 200){
        var obj=req.responseText;
        var h= JSON.parse(obj)
        var all=h['data']
         var div=document.getElementById('abcd');
        div.innerHTML="";

        var table= document.createElement('TABLE');

        var row=table.insertRow(0);
            var name=row.insertCell(0);
            var folder=row.insertCell(1)
            var date=row.insertCell(2);
            var time=row.insertCell(3);
            var status=row.insertCell(4);
            var check=row.insertCell(5);
            var size=row.insertCell(6);

            name.innerHTML ="FILE NAME";
            folder.innerHTML="FOLDER";
            date.innerHTML="DATE ";
            time.innerHTML="TIME";
            status.innerHTML="STATUS";
            check.innerHTML="CHECK";
            size.innerHTML="SIZE"

        for (var i=0; i< all.length;i++)
        {
            var row=table.insertRow(i+1);
            var name=row.insertCell(0);
            var folder=row.insertCell(1);
            var date=row.insertCell(2);
            var time=row.insertCell(3);
            var status=row.insertCell(4);
            var check=row.insertCell(5);
            var size=row.insertCell(6);

            name.innerHTML =all[i].name;
            folder.innerHTML=all[i].folder;
            date.innerHTML=all[i].date;
            time.innerHTML=all[i].time;
            status.innerHTML=all[i].status;
            check.innerHTML=all[i].check;
            size.innerHTML=all[i].size+" bytes";


        }
        table.className='table text-center table-hover'
        div.appendChild(table);
        }
    };
    req.open("GET",url,true);
    req.send();
}

function searchByDate()
{
    var file_date=document.getElementById('bydate').value;
    var req= new XMLHttpRequest();
    var url='searchDate?file_date='+file_date;
    req.onreadystatechange=function(){
        if(this.readyState == 4 && this.status == 200){
        var obj=req.responseText;
        var h= JSON.parse(obj)
        var all=h['data']

         var div=document.getElementById('abcd');
        div.innerHTML="";

        var table= document.createElement('TABLE');

        var row=table.insertRow(0);
            var name=row.insertCell(0);
            var folder=row.insertCell(1)
            var date=row.insertCell(2);
            var time=row.insertCell(3);
            var status=row.insertCell(4);
            var check=row.insertCell(5);
            var size=row.insertCell(6);

            name.innerHTML ="FILE NAME";
            folder.innerHTML="FOLDER";
            date.innerHTML="DATE ";
            time.innerHTML="TIME";
            status.innerHTML="STATUS";
            check.innerHTML="CHECK";
            size.innerHTML="SIZE"

        for (var i=0; i< all.length;i++)
        {
            var row=table.insertRow(i+1);
            var name=row.insertCell(0);
            var folder=row.insertCell(1);
            var date=row.insertCell(2);
            var time=row.insertCell(3);
            var status=row.insertCell(4);
            var check=row.insertCell(5);
            var size=row.insertCell(6);

            name.innerHTML =all[i].name;
            folder.innerHTML=all[i].folder;
            date.innerHTML=all[i].date;
            time.innerHTML=all[i].time;
            status.innerHTML=all[i].status;
            check.innerHTML=all[i].check;
            size.innerHTML=all[i].size+" bytes";


        }
        table.className='table text-center table-hover'
        div.appendChild(table);
        }
    };
    req.open("GET",url,true);
    req.send();
}

function betweenDate()
{
    var file_date1=document.getElementById('date1').value;
    var file_date2=document.getElementById('date2').value;
    var req= new XMLHttpRequest();
    var url='twoDates?file_date1='+file_date1+'&file_date2='+file_date2;
    req.onreadystatechange=function(){
        if(this.readyState == 4 && this.status == 200){
        var obj=req.responseText;
        var h= JSON.parse(obj)
        var all=h['data']

         var div=document.getElementById('abcd');
        div.innerHTML="";

        var table= document.createElement('TABLE');

        var row=table.insertRow(0);
            var name=row.insertCell(0);
            var folder=row.insertCell(1)
            var date=row.insertCell(2);
            var time=row.insertCell(3);
            var status=row.insertCell(4);
            var check=row.insertCell(5);
            var size=row.insertCell(6);

            name.innerHTML ="FILE NAME";
            folder.innerHTML="FOLDER";
            date.innerHTML="DATE ";
            time.innerHTML="TIME";
            status.innerHTML="STATUS";
            check.innerHTML="CHECK";
            size.innerHTML="SIZE"

        for (var i=0; i< all.length;i++)
        {
            var row=table.insertRow(i+1);
            var name=row.insertCell(0);
            var folder=row.insertCell(1);
            var date=row.insertCell(2);
            var time=row.insertCell(3);
            var status=row.insertCell(4);
            var check=row.insertCell(5);
            var size=row.insertCell(6);

            name.innerHTML =all[i].name;
            folder.innerHTML=all[i].folder;
            date.innerHTML=all[i].date;
            time.innerHTML=all[i].time;
            status.innerHTML=all[i].status;
            check.innerHTML=all[i].check;
            size.innerHTML=all[i].size+" bytes";


        }
        table.className='table text-center table-hover table-responsive-sm'
        div.appendChild(table);
        }
    };
    req.open("GET",url,true);
    req.send();
}

function timeInterval()
{
    var ival=document.getElementById('interval').value;
    var ch=document.getElementById('choose').value;
    var req= new XMLHttpRequest();
    var url='timeInterval?file_time='+ival+'&status='+ch;
    req.onreadystatechange=function(){
        if(this.readyState == 4 && this.status == 200){
        var obj=req.responseText;
        var h= JSON.parse(obj)
        var all=h['data']

         var div=document.getElementById('abcd');
        div.innerHTML="";

        var table= document.createElement('TABLE');

        var row=table.insertRow(0);
            var name=row.insertCell(0);
            var folder=row.insertCell(1)
            var date=row.insertCell(2);
            var time=row.insertCell(3);
            var status=row.insertCell(4);
            var check=row.insertCell(5);
            var size=row.insertCell(6);

            name.innerHTML ="FILE NAME";
            folder.innerHTML="FOLDER";
            date.innerHTML="DATE ";
            time.innerHTML="TIME";
            status.innerHTML="STATUS";
            check.innerHTML="CHECK";
            size.innerHTML="SIZE"

        for (var i=0; i< all.length;i++)
        {
            var row=table.insertRow(i+1);
            var name=row.insertCell(0);
            var folder=row.insertCell(1);
            var date=row.insertCell(2);
            var time=row.insertCell(3);
            var status=row.insertCell(4);
            var check=row.insertCell(5);
            var size=row.insertCell(6);

            name.innerHTML =all[i].name;
            folder.innerHTML=all[i].folder;
            date.innerHTML=all[i].date;
            time.innerHTML=all[i].time;
            status.innerHTML=all[i].status;
            check.innerHTML=all[i].check;
            size.innerHTML=all[i].size+" bytes";


        }
        table.className='table text-center table-hover'
        div.appendChild(table);
        }
    };
    req.open("GET",url,true);
    req.send();
}

function byTimeDate()
{
    var t=document.getElementById('byt').value;
    var d=document.getElementById('byd').value;
    var req= new XMLHttpRequest();
    var url='bytimeDate?file_time='+t+'&file_date='+d;
    req.onreadystatechange=function(){
        if(this.readyState == 4 && this.status == 200){
        var obj=req.responseText;
        var h= JSON.parse(obj)
        var all=h['data']

         var div=document.getElementById('abcd');
        div.innerHTML="";

        var table= document.createElement('TABLE');

        var row=table.insertRow(0);
            var name=row.insertCell(0);
            var folder=row.insertCell(1)
            var date=row.insertCell(2);
            var time=row.insertCell(3);
            var status=row.insertCell(4);
            var check=row.insertCell(5);
            var size=row.insertCell(6);

            name.innerHTML ="FILE NAME";
            folder.innerHTML="FOLDER";
            date.innerHTML="DATE ";
            time.innerHTML="TIME";
            status.innerHTML="STATUS";
            check.innerHTML="CHECK";
            size.innerHTML="SIZE"

        for (var i=0; i< all.length;i++)
        {
            var row=table.insertRow(i+1);
            var name=row.insertCell(0);
            var folder=row.insertCell(1);
            var date=row.insertCell(2);
            var time=row.insertCell(3);
            var status=row.insertCell(4);
            var check=row.insertCell(5);
            var size=row.insertCell(6);

            name.innerHTML =all[i].name;
            folder.innerHTML=all[i].folder;
            date.innerHTML=all[i].date;
            time.innerHTML=all[i].time;
            status.innerHTML=all[i].status;
            check.innerHTML=all[i].check;
            size.innerHTML=all[i].size+" bytes";


        }
        table.className='table text-center table-hover'
        div.appendChild(table);
        }
    };
    req.open("GET",url,true);
    req.send();
}




