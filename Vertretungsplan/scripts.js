function show_sidenav() {
    document.getElementById('sidenav').hidden = false
}
function hide_sidenav() {
    document.getElementById('sidenav').hidden = true
}
function open_selected(url) {
    if (url == "index.html") {
        if (window.location.pathname.split("/").pop() == "index.html") {
            window.open('./index.html','_self')
        }else {
            window.open('../index.html','_self')
        }
    }else {
        if (window.location.pathname.split("/").pop() == "index.html") {
            window.open('./Data/'.concat(url),'_self')
        }else {
            window.open('./'.concat(url),'_self')
        }
    }
}
function auto_scroll(original_width) {
    const table = document.getElementById("ubersicht_table")
    table.scrollLeft += 1.5
    if ((table.scrollLeft) > original_width) {
        table.scrollLeft -= original_width
    }
}

$(document).ready(function() {
    var url
    if (window.location.pathname.split("/").pop() == "index.html") {
        url = './data.json'
        ubersicht = document.getElementById('ubersicht').children[0]
    }else {
        url = '../data.json'
        ubersicht = document.getElementById('normal').children[0]
    }
    fetch(url)
        .then(response => {
            console.log(response)
            if (!response.ok) {
                throw new Error('Network response was not ok')
            }
            return response.json()
        })
        .then(data => {
            document.getElementById('date').innerHTML = data[0]
            klassen = ubersicht.children[0].children
            for (let key in data[1]) {
                for (let i = 0; i < klassen.length; i++) {
                    if (key == klassen[i].innerHTML) {
                        for (let stunden of Object.values(data[1][key])) {
                            info = Object.values(stunden)
                            var stunde = ubersicht.children[info[0]].children[i]
                            stunde.innerHTML = info[1].concat(' | ',info[2],' | ',info[3])
                            if (info[4]) {
                                stunde.classList.remove('normal')
                                stunde.classList.add('ausfall')
                            }else{
                                stunde.classList.remove('normal')
                                stunde.classList.add('vertretung')
                            }
                        }
                        break
                    }
                }
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error)
        })
    if (window.location.pathname.split("/").pop() == "index.html") {
        const original_table = document.getElementById("ubersicht")
        const original_width = original_table.scrollWidth
        const clones = screen.width/320
        const table = document.getElementById("ubersicht").children[0].children
        for (let i = 0; i < clones; i++) { 
            for (let j = 0; j < table.length; j++) {
                table[j].appendChild(table[j].children[i].cloneNode(true))
            }
        }
        setInterval(function(){auto_scroll(original_width)},10)
    }
})