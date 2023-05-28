import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from "react-bootstrap/Form";

export function LDAP(props) {
  const [show, setShow] = useState(true);
  const handleClose = () => setShow(false);
  const [username, setUsername] = useState("");
  const [pass, setPass] = useState("");

  // -- Pass the LDAP parameters -- //

  const handleSubmit = (e) => {
    e.preventDefault();
    handleClose();
    props.changeUsername(username);
    props.changePass(pass);
  };

  return (
    <>
      <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
      >
        <Modal.Header closeButton>
          <Modal.Title className="ldapSignIn">Sign In With LDAP</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Username</Form.Label>
              <Form.Control
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                type="username"
                placeholder="Enter username"
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                value={pass}
                onChange={(e) => setPass(e.target.value)}
                type="password"
                placeholder="Enter Password"
              />
            </Form.Group>
            <Button variant="primary" type="submit">
              Submit
            </Button>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          *I will not close if you click outside me. Don't even try to press
          escape key.
        </Modal.Footer>
      </Modal>
    </>
  );
}
