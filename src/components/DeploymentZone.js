import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

export function DeploymentZone({ changeDeployment }) {
  const params = useParams();
  const url = `https://prima.prod.bazaarvoice.com/api/client/config/${params.client}`;
  const [show, setShow] = useState(false);
  const [results, setResults] = useState([]);
  const [deployZone, setDeployZone] = useState("");
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  // -- fetch data -- //

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(url);
      const data = await response.json();
      setResults(data);
    }
    fetchData();
  }, [url]);

  return (
    <>
      <Button
        variant="secondary"
        onClick={handleShow}
        className="deploymentZone"
      >
        Deployment Zone
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Choose Deployment Zone</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <select
            onChange={(e) => {
              setDeployZone(e.target.value);
            }}
          >
            {results.length !== 0 &&
              results.deploymentZones.map((value) => {
                return <option key={value.id}>{value.id}</option>;
              })}
          </select>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button
            variant="primary"
            onClick={() => {
              changeDeployment(deployZone);
              handleClose();
            }}
          >
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}
