import { useState } from 'react'

import './App.css'

import FileUpload from './FileUpload'

import fileDownload from 'js-file-download'

function App() {

	const [google, setGoogle] = useState<File>()

	const [buk, setBuk] = useState<File>()
	
	async function sendFiles () {

		try {
	
			const formData = new FormData()
	
			if (google) formData.append("Google", google)
	
			if (buk) formData.append("Buk", buk)
	
			const options = {
				
				body: formData,
	
				method: 'POST'
	
			}
	
			const response = await fetch("http://127.0.0.1:5000/UploadFile", options)
			
			if (response.ok) {

				const data = await response.blob()

				fileDownload(data, "Google_Actualizado.xlsx")

			} else {

				console.error("Error", response.statusText)

			}

		} catch (error) {

			console.error('Error en la solicitud:', error);
			
		}

	}

	return (

		<main className='Container'>

			<section className='Section'>

				<FileUpload file={google} setFile={setGoogle} text='Carga o arrastra el excel de google' />

				<FileUpload file={buk} setFile={setBuk} text='Carga o arrastra el excel de buk'/>

			</section>

			<button className='Button' onClick={sendFiles} disabled={!google || !buk}>

				Generar documento

			</button>

		</main>

	)

}

export default App
