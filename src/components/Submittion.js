import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

export function Submittion(url) {
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  const [jiraKey, setJiraKey] = useState("");
  const [loading, setLoading] = useState(false);

  // -- fetch data -- //

  const fetchData = async () => {
    setLoading(true);
    await fetch(url.url)
    .then((res) => res.text())
    .then((jiraKeyValue) => {
      setJiraKey(jiraKeyValue);
    });
  setLoading(false);
};

  return (
    <>
      <Button variant="primary" onClick={() => {
        handleShow();
         fetchData();}
         } className="submittion">
        Submit
      </Button>

      <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
      >
        <Modal.Header closeButton>
          <Modal.Title className="submittionTitle">
            Posting Jira ticket
          </Modal.Title>
        </Modal.Header>
        <Modal.Body className="jiraLink">
          {loading ? (
            "Loading..."
          ) : (
            <a href={jiraKey} target="_blank" rel="noreferrer">
              {jiraKey}
            </a>
          )}
        </Modal.Body>
        <Modal.Footer>
          *I will not close if you click outside me. Don't even try to press
          escape key.
        </Modal.Footer>
      </Modal>
    </>
  );
}
