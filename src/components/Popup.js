import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

export function Popup(props) {
  const [show, setShow] = useState(true);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <>
      <Button variant="secondary" onClick={handleShow}>
        Choose The Environment
      </Button>

      <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
      >
        <Modal.Header closeButton>
          <Modal.Title>Choose The Environment</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Button
            variant="warning"
            onClick={() => {
              props.changeEnvironment("Staging");
              props.changeModeration("NO");
              handleClose();
            }}
          >
            Staging
          </Button>
          <Button
            variant="primary"
            onClick={() => {
              props.changeEnvironment("Production");
              props.changeModeration("YES");
              handleClose();
            }}
          >
            Production
          </Button>
        </Modal.Body>
        <Modal.Footer>
          *I will not close if you click outside me. Don't even try to press
          escape key.
        </Modal.Footer>
      </Modal>
    </>
  );
}
