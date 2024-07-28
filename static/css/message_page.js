let location = window.location
let wsStart = 'ws://'
let endpoint = wsStart +location.host + location.pathname

if(location.protocol === 'https') {
    wsStart = 'wss://'
}
endpoint = wsStart + location.host + location.pathname

var socket = new WebSocket(endpoint)

socket.onopen = asyn function(e: Event) {
    console.log('open', e)
}
socket.onmessage = asyn function(e: Event) {
    console.log('message', e)
}
socket.onerror = asyn function(e: Event) {
    console.log('error', e)
}
socket.onclose = asyn function(e: Event) {
    console.log('close', e)
}