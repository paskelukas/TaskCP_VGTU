import { useEffect, useState } from "react";

export function FetchRosetta(url) {
    const [results, setResults] = useState([]);

    // -- fetch data -- //
  
    useEffect(() => {
      async function fetchData() {
        const response = await fetch(url);
        const data = await response.json();
        setResults(data);
      }
      fetchData();
    }, [url]);
  
    return { results }
}