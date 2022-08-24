
function send_sms_brek(){
    document.querySelector("#sms_response_brek").innerHTML = "";

    document.querySelectorAll(".tr_data").forEach(row => {
        var name = row.querySelector(".tr_name").innerText;
        var phone = "+91"+row.querySelector(".tr_phone").innerText;
        var brek = row.querySelector(".tr_brek").innerText;
        if (brek === "YES"){
            var myHeaders = new Headers();
            myHeaders.append("api-key", "Aebdfef5ef9999c088831630a7ed5f6a3");
            myHeaders.append("Content-Type", "application/json");

            var r = (Math.random() + 1).toString(36).substring(7).toUpperCase();
            console.log("Sender:", r)

            var raw = JSON.stringify({
            "body": "Hello "+name+", Your Breakfast will be available in the Kaleyra Cafeteria. Admin team: "+r,
            "sender": r,
            "to": phone,
            "type": "TXN",
            "template_id": "1107165959856139086"
            });

            var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
            };

            fetch("https://api.in.kaleyra.io/v1/HXIN1741995210IN/messages", requestOptions)
            .then(response => response.text())
            .then((result) => {
                console.log(result);
            })
            .catch(error => console.log('error', error));
        }
        document.querySelector("#sms_response_brek").innerHTML = "Successfully sent breakfast messages.";
    });
}

function send_sms_snak(){
    document.querySelector("#sms_response_snak").innerHTML = "";

    document.querySelectorAll(".tr_data").forEach(row => {
        var name = row.querySelector(".tr_name").innerText;
        var phone = "+91"+row.querySelector(".tr_phone").innerText;
        var snak = row.querySelector(".tr_snak").innerText;
        if (snak === "YES"){
            var myHeaders = new Headers();
            myHeaders.append("api-key", "Aebdfef5ef9999c088831630a7ed5f6a3");
            myHeaders.append("Content-Type", "application/json");

            var r = (Math.random() + 1).toString(36).substring(7).toUpperCase();
            console.log("Sender:", r)

            var raw = JSON.stringify({
            "body": "Hello "+name+", Your Snacks will be available in the Kaleyra Cafeteria. Admin team: "+r,
            "sender": r,
            "to": phone,
            "type": "TXN",
            "template_id": "1107165959856139086"
            });

            var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
            };

            fetch("https://api.in.kaleyra.io/v1/HXIN1741995210IN/messages", requestOptions)
            .then(response => response.text())
            .then((result) => {
                console.log(result);
            })
            .catch(error => console.log('error', error));
        }
        document.querySelector("#sms_response_snak").innerHTML = "Successfully sent Snacks messages.";
    });
}