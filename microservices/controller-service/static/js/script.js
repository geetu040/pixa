load_user_data();
// populate({
//     "username": "geetu",
//     "storage_usage": 1.4659414291381836,
//     "bandwidth_usage": 0,
//     "images_links": [
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/65ac6b20-1bcc-48e9-ae70-fe29b441b6be.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/47478cfa-f4ee-4d11-b269-2463ee3c0852.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/3acd2e11-4551-498c-b3ff-1d0fbd927dd9.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/350b35f3-d40c-4607-ad92-1b3277cb93ce.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/c09d6fc0-2e10-403b-a332-12a9b59e81b9.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/favicon.png?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/49de56f4-ceb9-445d-b8c1-285d507f76b3.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/c90f49c9-baa4-46ec-9c73-eb6f4148ebef.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/7e33dcb6-1316-4568-9c8b-d36a6f87b453.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/0d5127b6-a56d-4651-8ad1-bff9c9288adc.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/3f5bfec3-c3c8-4708-b87d-2296454ec197.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/12c0d54e-37e0-4905-bdd5-e2547168d0f8.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D",
//         "https://pixastorage.file.core.windows.net/user-imgs/geetu/0be81184-32b1-45c0-8dfc-47d2e9e308f5.jpg?sv=2022-11-02&ss=bfqt&srt=o&sp=rwdlacupiytfx&se=2024-12-11T01:52:41Z&st=2023-12-10T17:52:41Z&spr=https,http&sig=MBKGJrRVKtnnBIXtcQjAwruwZ2RPZCcANRvUKJFerHg%3D"
//     ]
// })

// ====> UTILS

function get_token() {
	let token = localStorage.getItem(LOCAL_STORAGE_ITEM);
	if (! token) {
		window.location = "/login";
	}
	return token;
}

function logout() {
	let answer = window.confirm("Do you want to Log Out?");
	if (answer) {
		localStorage.removeItem(LOCAL_STORAGE_ITEM);
		window.location = "/login";
	}
}

async function send_request(url, content_type, body) {
	let token = get_token();
	
	let headers = {
		'Authorization': `Bearer ${token}`,
	}
	if (content_type) {
		headers['Content-Type'] = content_type;
	}
	startLoader();
	const response = await fetch(url, {
		method: 'POST',
		headers: headers,
		body: body,
	})
	const data = await response.json();
	stopLoader();
	
	if (response.status == 200) {
		console.log(data);
		populate(data);
	} else {
		console.log(data);
	}
}

function populate(data) {

	document.getElementsByClassName("nav-close")[0].click();
	document.getElementById("username").innerText = data.username;
	document.getElementById("storage_usage").innerText = Math.round(data.storage_usage*10)/10;
	document.getElementById("bandwidth_usage").innerText = Math.round(data.bandwidth_usage * 1000) / 1000;

	let images_links = data.images_links;
	let dashboard_html = `<li class="grid-sizer"></li><!-- for Masonry column width -->`;
	let hover_html = ``;
	let timestamp = Date.now();		// to load images from cache
	images_links.forEach(link => {
		dashboard_html += `
		<li>
			<figure>
				<img src="${link}&timestamp=${timestamp}" alt="image"/>
			</figure>
		</li>
		`
		hover_html += `
		<li>
			<figure>
				<figcaption>
					<i class="fas fa-trash-alt" onclick="delete_image('${link}')"></i>
				</figcaption>
				<img src="${link}&timestamp=${timestamp}" alt="image"/>
			</figure>
		</li>
		`
	});
	document.getElementById("dashboard").innerHTML = dashboard_html;
	document.getElementById("hover-dashboard").innerHTML = hover_html;
	new CBPGridGallery(document.getElementById('grid-gallery'));

}

// ====> APIS

function load_user_data() {
	let url = CONTROLLER_EPS.load_user_data;
	send_request(url, 'application/json', JSON.stringify({}));
}

function delete_image(link) {
	let url = CONTROLLER_EPS.delete_image;
	send_request(url, 'application/json', JSON.stringify({"link": link}));
}

function upload_image(file) {
	let url = CONTROLLER_EPS.upload_image;
    let formData = new FormData();
    formData.append("file", file);
	send_request(url, null, formData);
}

// ====> DOM

function upload_image_btn() {
	// Trigger click event on the file input
	if (parseFloat(document.getElementById("storage_usage").innerText) >= 1000) {
		alert("You have utilized all storage");
		return;
	}
	if (parseFloat(document.getElementById("bandwidth_usage").innerText) >= 25) {
		alert("You have utilized dailty bandwidth");
		return;
	}
	document.getElementById('fileInput').click();
}

function handleFile() {
	// Handle the selected file here
	const fileInput = document.getElementById('fileInput');
	const selectedFile = fileInput.files[0];

	if (selectedFile) {
		upload_image(selectedFile)
	}
}

function closePopup() {
	// Close the popup
	document.getElementById('uploadPopup').style.display = 'none';
}

