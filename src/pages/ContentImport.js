import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Table } from "react-bootstrap";
import Button from "react-bootstrap/Button";

import {
  Popup,
  FetchRosetta,
  DeploymentZone,
  FetchMinesweeper,
  FileSubmission,
  Submittion,
} from "../components";

export const ContentImport = () => {
  const params = useParams();
  const navigate = useNavigate();
  const [displayCode, setDisplayCode] = useState("main_site");
  const { results } = FetchRosetta(
    `https://prima.prod.bazaarvoice.com/api/client/deploymentConfig/${params.client}/${displayCode}/PRODUCTION`
  );
  const { sweeper } = FetchMinesweeper(params);
  const [environment, setEnvironment] = useState("Staging");
  const [selectedOption, setSelectedOption] = useState("Option 1");
  const [inputValue, setInputValue] = useState("none");
  const [selectValue, setSelectValue] = useState("");
  const [sweeperValue, setSweeperValue] = useState(
    "https://minesweeper.prod.bazaarvoice.com/results/"
  );
  const [feedValue, setFeedValue] = useState("");
  const [sfcaseValue, setSFCaseValue] = useState("");
  const [moderateValue, setModerateValue] = useState("NO");
  const [contentCodes, setContentCodes] = useState("IMP");
  const [Attachment, setAttachment] = useState(null);
  const [checkedValues, setChekcedValues] = useState(["review"]);
  const [isFirstRender, setFirstRender] = useState(true);

  // -- handle deployment zone hook -- //

  const changeDeployment = (site) => {
    site !== displayCode ? setDisplayCode(site) : setDisplayCode("main_site");
  };

  // -- append content type array -- //

  const handleChange = (event) => {
    const { value, checked } = event.target;
    if (checked) {
      setChekcedValues((pre) => [...pre, value]);
    } else
      setChekcedValues((pre) => {
        return [...pre.filter((skill) => skill !== value)];
      });
  };

  // -- handle attachment -- //

  const fileInfo = (file) => {
    //console.log(file);
    setAttachment(file);
  };

  // -- send a request to a backend on a submit -- //

  useEffect(() => {
    if (isFirstRender) {
      async function fetchData() {
        await fetch(
          `/content_import_sftp/${params.client
          }/${environment}/${localStorage.getItem(
            "Username"
          )}/${localStorage.getItem("Password")}`
        )
          .then((res) => res.text())
          .then((selectedValue) => {
            setSelectValue(selectedValue);
            console.log(selectValue);
          });
      }
      fetchData();
      async function fetchDataFilename() {
        await fetch(
          `/content_import_sftp_filename/${params.client
          }/${environment}/${localStorage.getItem(
            "Username"
          )}/${localStorage.getItem("Password")}`
        )
          .then((res) => res.text())
          .then((selectedValue) => {
            setFeedValue(selectedValue);
            console.log(feedValue);
          });
      }
      fetchDataFilename()
      setFirstRender(false);
    } else {
      async function fetchData() {
        await fetch(
          `/content_import_sftp/${params.client
          }/${environment}/${localStorage.getItem(
            "Username"
          )}/${localStorage.getItem("Password")}`
        )
          .then((res) => res.text())
          .then((selectedValue) => {
            setSelectValue(selectedValue);
            console.log(selectValue);
          });
      }
      fetchData();
      async function fetchDataFilename() {
        await fetch(
          `/content_import_sftp_filename/${params.client
          }/${environment}/${localStorage.getItem(
            "Username"
          )}/${localStorage.getItem("Password")}`
        )
          .then((res) => res.text())
          .then((selectedValue) => {
            setFeedValue(selectedValue);
            console.log(feedValue);
          });
      }
      fetchDataFilename()
    }
  }, [environment]);

  // -- Table -- //

  const rows = [
    { id: 1, col1: "Client", col2: `${params.client}` },
    { id: 2, col1: "Environment", col2: `${environment}` },
    {
      id: 3,
      col1: "Source",
      col2: (
        <select
          value={selectedOption}
          onChange={(e) => setSelectedOption(e.target.value)}
        >
          <option value="Option 1">New Client (external)</option>
          <option value="Option 2">PWR</option>
          <option value="Option 3">BV</option>
        </select>
      ),
    },
    {
      id: 4,
      col1: "Feed File",
      col2: (
        <input
          type="text"
          value={feedValue}
          onChange={(e) => setFeedValue(e.target.value)}
        />
      ),
    },
    {
      id: 5,
      col1: "Fingerprint/Iovation File",
      col2: (
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
      ),
    },
    {
      id: 6,
      col1: "Expected # of content",
      col2: (
        <input
          type="text"
          value={selectValue}
          onChange={(e) => setSelectValue(e.target.value)}
        />
      ),
    },
    {
      id: 7,
      col1: "Included content types",
      col2: (
        <div>
          <input
            type="checkbox"
            id="review"
            name="review"
            value="review"
            defaultChecked
            onChange={handleChange}
          />
          <label htmlFor="review">Review</label>
          <input
            type="checkbox"
            id="question"
            name="question"
            value="question"
            onChange={handleChange}
          />
          <label htmlFor="question">Question</label>
          <input
            type="checkbox"
            id="answer"
            name="answer"
            value="answer"
            onChange={handleChange}
          />
          <label htmlFor="answer">Answer</label>
          <input
            type="checkbox"
            id="comment"
            name="comment"
            value="comment"
            onChange={handleChange}
          />
          <label htmlFor="comment">Comment</label>
          <input
            type="checkbox"
            id="profile"
            name="profile"
            value="profile"
            onChange={handleChange}
          />
          <label htmlFor="profile">Profile</label>
        </div>
      ),
    },
    {
      id: 8,
      col1: "Display code",
      col2: `${results?.clientDeploymentConfigs?.implementations?.main?.displayCode}`,
    },
    {
      id: 9,
      col1: "Moderate (new)?",
      col2: (
        <input
          type="text"
          value={moderateValue}
          onChange={(e) => setModerateValue(e.target.value)}
        />
      ),
    },
    {
      id: 10,
      col1: "Content Codes",
      col2: (
        <input
          type="text"
          value={contentCodes}
          onChange={(e) => setContentCodes(e.target.value)}
        />
      ),
    },
    {
      id: 11,
      col1: "SFCase(s), SOW",
      col2: (
        <input
          type="text"
          value={sfcaseValue}
          onChange={(e) => setSFCaseValue(e.target.value)}
        />
      ),
    },
    {
      id: 12,
      col1: "Minesweeper Result",
      col2: (
        <input
          type="text"
          value={sweeperValue + sweeper?.list?.[0]?._id}
          onChange={(e) => setSweeperValue(e.target.value)}
        />
      ),
    },
    {
      id: 13,
      col1: "Client Provided Import Files",
      col2:
        Attachment !== null
          ? Attachment.name + ", Attached below"
          : "No files have been provided",
    },
  ];

  return (
    <main>
      <div className="component">
        <Button
          variant="secondary"
          className="back"
          onClick={() => {
            navigate(`/${params.client}`);
          }}
        >
          Back
        </Button>
        {params.client}({results?.clientDeploymentConfigs?.cluster}@
        {environment === "Staging" ? "stg" : "prod"}) | content import
        <Table striped bordered hover size="sm">
          <tbody>
            {rows.map((row) => (
              <tr key={row.id}>
                <td>{row.col1}</td>
                <td>
                  {row.id === 5 ? (
                    <input
                      type="text"
                      value={inputValue}
                      onChange={(e) => setInputValue(e.target.value)}
                    />
                  ) : row.id === 7 ? (
                    row.col2
                  ) : (
                    row.col2
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
      <Popup
        changeEnvironment={(environment) => setEnvironment(environment)}
        changeModeration={(moderation) => setModerateValue(moderation)}
      />
      <DeploymentZone changeDeployment={changeDeployment} />
      <FileSubmission fileInfo={fileInfo} />
      <Button
        variant="secondary"
        className="documentation"
        onClick={() => {
          window.open(
            "https://bazaarvoice.atlassian.net/wiki/spaces/DEV/pages/6801883558/Service+Request+-+Import+Content",
            "_blank"
          );
        }}
      >
        Documentation
      </Button>
      <Submittion
        url={`/jiraapi/${params.client}/${results?.clientDeploymentConfigs?.cluster}/${environment}/${selectedOption}/${feedValue}/${inputValue}/${selectValue}/${checkedValues}/${results?.clientDeploymentConfigs?.implementations?.main?.displayCode}/${moderateValue}/${contentCodes}/${sfcaseValue}/${sweeper?.list?.[0]?._id}`}
      />
    </main>
  );
};
