// configuring endpoints

// converting from client at 80 to server at 8080
const CONTROLLER_API = ``
// const CONTROLLER_API = `${window.location.protocol}//${window.location.hostname}:8080`
// const CONTROLLER_API = "http://localhost:8080"

const CONTROLLER_EPS = {
	"auth_user": `${CONTROLLER_API}/auth_user`,
	"load_user_data": `${CONTROLLER_API}/load_user_data`,
	"delete_image": `${CONTROLLER_API}/delete_image`,
	"upload_image": `${CONTROLLER_API}/upload_image`,
}
const LOCAL_STORAGE_ITEM = "pixa-token";

// ====> LOADER

function startLoader() {
	document.getElementById('loaderContainer').style.display = 'block';
	document.body.classList.add('blur');
}

function stopLoader() {
	document.getElementById('loaderContainer').style.display = 'none';
	document.body.classList.remove('blur');
}