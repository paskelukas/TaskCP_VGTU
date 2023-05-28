import React, { useEffect, useState } from "react";
import SearchIcon from "@mui/icons-material/Search";
import CloseIcon from "@mui/icons-material/Close";

export function SearchClients({ placeholder }) {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  // -- fetch data -- //

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(
        `https://prima.prod.bazaarvoice.com/api/clients/search/${query}`
      );
      const data = await response.json();
      setResults(data);
    }
    fetchData();
  }, [query]);

  // -- if search form is empty, do not show any results -- //

  function handleInputChange(event) {
    if (event.target.value === "") {
      setResults([]);
      setQuery("");
    } else {
      setQuery(event.target.value);
    }
  }

  // -- clear the input -- //

  const clearInput = () => {
    setResults([]);
    setQuery("");
  };

  return (
    <div className="search">
      <div className="searchInputs">
        <input
          type="text"
          placeholder={placeholder}
          value={query}
          onChange={handleInputChange}
        />
        <div className="searchIcon">
          {results.length === 0 ? (
            <SearchIcon />
          ) : (
            <CloseIcon id="clearBtn" onClick={clearInput} />
          )}
        </div>
      </div>
      {results.length !== 0 && (
        <div className="dataResult">
          {results.map((value) => {
            return (
              <a className="dataItem" href={value.name} key={value._id}>
                <p>{value.name}</p>
              </a>
            );
          })}
        </div>
      )}
    </div>
  );
}
