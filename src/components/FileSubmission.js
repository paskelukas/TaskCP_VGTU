import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import axios from "axios";
import { useParams } from "react-router-dom";

export function FileSubmission({ fileInfo }) {
  const params = useParams();
  const [, setfileURL] = useState("");
  const [selectedFile, setselectedFile] = useState(null);
  const [uploadedFile, setuploadedFile] = useState({});
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  const [file, setFile] = useState();
  const [isUploading, setisUploading] = useState(false);
  const [isFileUploaded, setisFileUploaded] = useState(false);
  const [uploadProgress, setuploadProgress] = useState(0);

  let uploadInput = React.createRef();

  // -- Handle the file to backend -- //

  const handleFile = async (ev) => {
    ev.preventDefault();

    const selectedFileList = [];
    for (let i = 0; i < ev.target.files.length; i++) {
      selectedFileList.push(ev.target.files.item(i));
    }
    setselectedFile(selectedFileList);

    let file = ev.target.files[0];
    setFile(file);

    setisUploading(true);
    const data = new FormData();
    // Append the file to the request body
    for (let i = 0; i < uploadInput.files.length; i++) {
      data.append("file", uploadInput.files[i], uploadInput.files[i].name);
    }

    try {
      const config = {
        onUploadProgress: (progressEvent) => {
          const { loaded, total } = progressEvent;
          setuploadProgress(Math.round((loaded / total) * 100));
        },
      };
      const response = await axios.post(
        `http://localhost:5000/${params.client}/upload`,
        data,
        config
      );
      const body = response.data;
      console.log(body);
      setfileURL(`http://localhost:5000/${params.client}/${body.filename}`);
      if (response.status === 200) {
        setisFileUploaded(true); // flag to show the uploaded file
        setisUploading(false);
        setuploadedFile(selectedFile); // set the uploaded file to show the name
      }
    } catch (error) {
      console.error(error);
      setisUploading(false);
    }
  };

  return (
    <>
      <Button
        variant="secondary"
        onClick={handleShow}
        className="deploymentZone"
      >
        Add Attachment
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Client Provided Import File</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <div className="fileSubmission">
            <label>Select File</label>
            <input type="file" name="file" onChange={(ev) => handleFile(ev)} />
          </div>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button
            variant="primary"
            onClick={() => {
              fileInfo(file);
              handleClose();
            }}
          >
            Upload
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}
