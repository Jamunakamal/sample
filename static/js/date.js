function getDate(){
    const d= new Date();
    return d.toLocaleString();
}
function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(savePosition, positionError, {timeout:10000});
        } else {
            //Geolocation is not supported by this browser
        }
    
}