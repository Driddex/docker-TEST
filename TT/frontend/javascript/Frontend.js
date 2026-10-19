async function def() {
    console.log("Clicked");

    let output = document.getElementById('gg')
    let input_text = document.getElementById('ggg')

    output.textContent = 'Waiting For Answer'
    data = input_text.value

    try {

        const response = await fetch('http://localhost/p', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: parseInt(data) })
        });

        const serverData = await response.json();

        console.log(serverData);
        output.textContent = 'Succesfully got a answer from server...'

    } catch (error) {
        console.log('error')
    }
}