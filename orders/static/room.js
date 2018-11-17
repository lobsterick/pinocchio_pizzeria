document.addEventListener('DOMContentLoaded', () => {

    // Load all messages via Ajax request
    fetchPostsOnLoad();

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When you add new message with submit, server should append it to the room's messages
    socket.on('connect', () => {
        document.querySelector("#new_message").onsubmit = function () {
            var new_message_body = document.querySelector("#new_message_body").value;
            if (!(new_message_body === '')) {
                socket.emit("new_message_submit", new_message_body);
                document.querySelector("#new_message_body").value = '';
            }
            return false
        }
    });


    // When a new message is announced, reload all messages on page
    socket.on('update_messages', updated_list => loadMessages(updated_list));

});

function loadMessages(updated_list) {
    const last_room = window.location.href.split("/").pop();
    if (updated_list[last_room]) {
        var messages_last_100 = document.getElementById("messages_last_100");
        messages_last_100.innerHTML = "";
        var posts;
        for (posts in updated_list[last_room]) {
            var timestamp = new Date(updated_list[last_room][posts][0] * 1000).toLocaleString();
            var post = document.createElement('div');
            var inHTML = '<div class="post"><span style=\'color: #946e09; font-weight:bold\'>';
            inHTML += updated_list[last_room][posts][1];
            inHTML += '</span> (';
            inHTML += timestamp;
            inHTML += ") </br>";
            inHTML += updated_list[last_room][posts][2];
            inHTML += "</div>";
            post.innerHTML = inHTML;
            messages_last_100.appendChild(post);
        }
        window.scrollTo(0, document.body.scrollHeight);
        return false
    }
}

function fetchPostsOnLoad(){
    const request = new XMLHttpRequest();
    const room = window.location.href.split("/").pop();
    const requestAdress = `/room/${room}/json`;
    request.open('GET', requestAdress, true);
    request.addEventListener('load', function() {
        const data = JSON.parse(request.responseText);
        // Present all posts on page
        if (data.success) {
            loadMessages(data);
            return false
        }
        else {
            alert("Error when trying to fetch data");
            return false
        }
    });

    request.send();

}