//function textif() {
//gewinncodes
  //var jain = ["0135","0257","0328","0429","0537","0613","0783","0835","0962","1046","1184","1286","1307","1438","1509","1650","1748","1835","1936","2037","2193","2239","2358","2438",];
//input code
  //var code = prompt('Code:','');
//vergleichen
  //var win = jain.includes(code.toLowerCase());
//entscheidung
  //if (win) {
    //window.open('./Documents/gewinn.html');
  //}else {
    //window.open('./Documents/niete.html');
  //}



  //window.open('./Documents/gewinn.html');
//}


function eins(id) {
//gewinncodes
  var jain = ["0135","0257","0328","0429","0537","0613","0783","0835","0962","1046","1184","1286","1307","1438","1509","1650","1748","1835","1936","2037","2193","2239","2358","2438",];
//input code
  var code = prompt('Code:','');
//vergleichen
  //var win = jain.includes(code.toLowerCase());
//entscheidung
  if (code==jain[id]) {
    window.open('./Documents/gewinn.html','_self');
  }else {
    window.open('./Documents/niete.html','_self');
  }

}
