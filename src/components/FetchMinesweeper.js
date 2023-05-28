import { useEffect, useState } from "react";

export function FetchMinesweeper(params) {
    const url = `https://minesweeper-backend.prod.bazaarvoice.com/api/results?client=${params.client}`;
    const [sweeper, setSweeper] = useState([]);
  
    // -- fetch data -- //
    
    useEffect(() => {
      async function fetchData() {
        const response = await fetch(url);
        const data = await response.json();
        setSweeper(data);
      }
      fetchData();
    }, [url]);
  
    return { sweeper }
}