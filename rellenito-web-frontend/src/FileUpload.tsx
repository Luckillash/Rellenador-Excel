import React, { DragEvent, ChangeEvent, Dispatch, SetStateAction } from "react";

interface IProps {

    file: File | undefined,

    setFile: Dispatch<SetStateAction<File | undefined>>,

    text: string

}

export default function FileUpload({ file, setFile, text }: IProps) {

    const [dragActive, setDragActive] = React.useState(false);

    const inputRef = React.useRef<HTMLInputElement>(null);
    
    const handleDrag = function(e: DragEvent<HTMLFormElement | HTMLDivElement>) {
        
        e.preventDefault();
        
        e.stopPropagation();
        
        if (e.type === "dragenter" || e.type === "dragover") {
            
            setDragActive(true);
        
        } else if (e.type === "dragleave") {
            
            setDragActive(false);
        
        }

    };
    
    // triggers when file is dropped
    const handleDrop = function(e: DragEvent<HTMLFormElement | HTMLDivElement>) {

        e.preventDefault();

        e.stopPropagation();

        setDragActive(false);

        if (e.dataTransfer.files && e.dataTransfer.files[0]) {

            setFile(e.dataTransfer.files[0]);

        }

    };
    
    // triggers when file is selected with click
    const handleChange = function(e: ChangeEvent<HTMLInputElement>) {

        e.preventDefault();

        if (e.target.files && e.target.files[0]) {

            setFile(e.target.files[0]);

        }

    };
    
  // triggers the input when the button is clicked
    const onButtonClick = () => {

        if(inputRef.current) inputRef.current.click();

    };
    
    return (

        <form id="form-file-upload" onDragEnter={handleDrag} onSubmit={(e) => e.preventDefault()}>
            
            <input ref={inputRef} type="file" id="input-file-upload" multiple={false} onChange={handleChange} accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" />
                
                <label id="label-file-upload" htmlFor="input-file-upload" className={dragActive ? "drag-active" : "" }>
                    
                    <div>

                        { file ? 
                        
                            <p>{ file.name }</p>
                    
                            :

                            <>
                            
                                <p>{ text }</p>
                                
                                <button className="upload-button" onClick={onButtonClick}>Upload a file</button>
                            
                            </>

                        }
                        
                    </div> 
                
                </label>
            
            { dragActive && <div id="drag-file-element" onDragEnter={handleDrag} onDragLeave={handleDrag} onDragOver={handleDrag} onDrop={handleDrop}></div> }
        
        </form>
    
    );

}