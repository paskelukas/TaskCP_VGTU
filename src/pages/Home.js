import { useState, useEffect } from "react";
import { SearchClients, LDAP } from "../components";

export const Home = () => {
  const [username, setUsername] = useState("");
  const [pass, setPass] = useState("");

  // -- Set LDAP credentials -- //

  useEffect(() => {
    function setLocalValues() {
      localStorage.setItem("Username", username);
      localStorage.setItem("Password", pass);
    }
    setLocalValues();
    console.log();
  }, [username, pass]);

  return (
    <main>
        <LDAP
          changeUsername={(username) => setUsername(username)}
          changePass={(pass) => setPass(pass)}
        />
        <div id="home-container" className="component">
          Welcome to TaskCP
          <SearchClients placeholder="Clients instance" />
        </div>
    </main>
  );
};
