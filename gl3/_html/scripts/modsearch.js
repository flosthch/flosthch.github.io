// Funktionen für die Modulsuche

var STRModulNameArtikel = 'Der';
var STRModulName =  'Buchlink';
var MSGGueltig = 'Bitte einen g%FCltigen '+STRModulName+' in das Suchfeld eingeben!';


function fnStartSearch(modName) {
	// Zugriff auf exakte Moduleingabe
	var module = sIndex[modName];	
	if (!module) {		
		// Transformation erzeugt doppelten Eintrag in Kleinschreibweise
		// Deshalb erneuter Zugriff auf Kleinschreibweise 
		module = sIndex[modName.toLowerCase()];
	}
	if(module) {

		// Sonderbehandlung FLV-Dateien
		// Bei FLV soll der zugeh. gleichnamige Player (SWF-Datei) aufgerufen werden
		var dateiend = module.substring(module.length-4,module.length);
		dateiend = dateiend.toLowerCase();
		if(dateiend=='.flv') {
			module = module.replace(/.flv/g,".swf"); // flv- durch swf-Datei austauschen
		}
		fnOpenModuleWindow(module);
	} 
	else
    	alert(STRModulNameArtikel +' '+ STRModulName +' "' + modName + '" wurde nicht gefunden!');


}


function fnOpenModuleWindow(location) {
	moduleWindow = window.open(location, "_blank");
	//moduleWindow.focus(); //erzeugt bei nicht-HTML-Dateien Fehler
}



function fnCreateModFrm() {
	//Suchformular aufbauen
	var SelfURL = document.location.href;
	document.writeln("<form method=\"get\" action=\"" + SelfURL + "\" name=\"modsearchFrm\" id=\"modsearchFrm\" accept-charset=\"ISO-8859-1\">");
	
	document.writeln("<input name=\"mod\" value=\"" + fnGetMod("anzeige") + "\" type=\"text\" size=\"5\" maxlength=\"10\" />");
	document.writeln("<img src=\"layout/buPfeil.gif\" alt=\"Pfeil\" width=\"9\" height=\"12\" />");
	document.writeln("<a href=\"javascript:document.modsearchFrm.submit();\" titel=\"" + STRModulName + " &ouml;ffnen\">"+STRModulName+"</a>");

	document.writeln("<a id=\"modSearchAnchor\">");
	document.writeln("</a>");

	document.writeln("</form>");
	//Suche auswerten
	var aModule = fnGetMod("suche");
	if (aModule) {
		fnStartSearch(aModule);
	}
}




function fnGetMod(aStati) {
	//Suchestring aus URL abspalten
	var ModuleString="";
	var SearchString = document.location.href;
	var SearchKey = "mod=";
	var aIndex = SearchString.indexOf(SearchKey) + SearchKey.length;


	if (aIndex > SearchKey.length){
//alert('aIndex: '+aIndex+' SearchKey.length: '+SearchKey.length);
		SearchString=SearchString.substr(aIndex, SearchString.length);
		
		//Hexzeichen umwandeln
		SearchString = unescape(SearchString);
		//Leerzeichen wird als '+' dargestellt, wieder zurueck wandeln
		SearchString = SearchString.replace(/\+/g," ");

		if (SearchString.length>0){
			ModuleString=SearchString;
		}else if(aStati=="suche"){
			alert(unescape(MSGGueltig));
		}

	}
	return(ModuleString);
}