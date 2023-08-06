import React, { useState, useEffect } from "react";

const Search = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:5000?query=${query}`)
      .then(results => {console.log(results); return results.data})
      .then(data => {
        console.log(data)
        const {name} = data.results[0];
        setFirstName(name.first);
        setLastName(name.last);
      });
  }, [query]); // <-- Have to pass in [] here!


  return (
    <div>
      <input
        type="text"
        placeholder="Enter a query"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <ul>
        {results.map((result, index) => (
          <li key={index}>{result}</li>
        ))}
      </ul>
    </div>
  );
};

export default Search;