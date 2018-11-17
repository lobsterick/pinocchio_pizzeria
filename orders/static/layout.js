document.addEventListener('DOMContentLoaded', () => {

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);


    // When you add new room with submit, server should update it's table of rooms
    socket.on('connect', () => {
            document.querySelector("#new_room_form").onsubmit = function () {
                let new_room_name = document.querySelector("#new_room_name").value;
                new_room_name = new_room_name.replace(/[^a-z0-9]/gi, ''); // sanitizing
                if (!(new_room_name === '')) {
                    socket.emit("update_room_list", new_room_name)
                }
            }
        }
    );

    // When a new room is announced, add to the dropdown rooms list
    socket.on('Update room list', data => {
        let dropdownlist = document.getElementById("dropdown_rooms_list");
        let opt = document.createElement('option');
        opt.innerHTML = data;
        opt.value = `/room/${data}`;
        dropdownlist.appendChild(opt)
    });
});

// When user is reloading page, compare server data with his localStorage and make changes
function checkReturningUser() {
    var nickname = localStorage.getItem("nickname");
    var last_room = localStorage.getItem("last_room");
    console.log(`Nickname: ${nickname}, last room: ${last_room}`);
    var postuser;
    if (!(nickname === null && last_room === null)) {
        console.log("Nickname and Last_room exist in localStorage. Sending request to check");
        var data = new FormData();
        data.append('nickname', nickname);
        data.append('last_room', last_room);
        postuser = new XMLHttpRequest();
        postuser.open('POST', '/checklogin', true);
        postuser.onload = function () {
            data = JSON.parse(postuser.responseText);
            if (!(data.status)){
                location.reload();
                console.log("Data from localStorage didn't match server data, but server-data is changed to match localStorage data. Reloading page. ");
                return false
            } else {
                console.log("Everything ok!");
                localStorage.last_room = data.last_room;
                return false}
        };
        postuser.send(data);
    }
    else {
        console.log("No login data in localStorage, checking if server know anything about me");
        postuser = new XMLHttpRequest();
        postuser.open('GET', '/checklogin', true);
        postuser.onload = () => {
            data = JSON.parse(postuser.responseText);
            if (data.logged) {
                console.log("There is info about me on server, restoring my localStorage.");
                localStorage.nickname = data.nickname;
                localStorage.last_room = data.last_room;
                console.log(`Restored nickname: ${localStorage.nickname}, restored last room: ${localStorage.last_room}`);
                return false
            }
            else {
                console.log("I was not logged at all! And i'm still unlogged");
                return false
            }
        };
        postuser.send();
    }
}

checkReturningUser();