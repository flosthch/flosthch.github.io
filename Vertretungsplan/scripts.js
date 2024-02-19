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
    }else {
        url = '../data.json'
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
            console.log(data)
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