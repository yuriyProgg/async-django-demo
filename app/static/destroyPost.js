function destroyPost(id, url, csrf_token) {
	fetch(url, {
		method: 'DELETE',
		headers: {
			'X-CSRFToken': csrf_token,
			'Content-Type': 'application/json',
		},
	}).then(response => {
		if (response.ok) document.getElementById(`post-${id}`).remove()
	})
}
