import './App.css';
import TextInput from './components/TextInput'
import ReactTwitterLogin from "react-twitter-login";
import { useState } from 'react';

function App() {
  const authHandler = (error, data) => {
    if (error) return console.error(error);
    console.log(data);
  };

  const TWITTER_CLIENT_ID = "" // give your twitter client id here

  // twitter oauth Url constructor
  function getTwitterOauthUrl() {
    const rootUrl = "https://twitter.com/i/oauth2/authorize";
    const options = {
      redirect_uri: "https://four-exchange.surge.sh", // client url cannot be http://localhost:3000/ or http://127.0.0.1:3000/
      client_id: TWITTER_CLIENT_ID,
      state: "state",
      response_type: "code",
      code_challenge: "y_SfRG4BmOES02uqWeIkIgLQAlTBggyf_G7uKT51ku8",
      code_challenge_method: "S256",
      scope: ["users.read", "tweet.read", "follows.read", "follows.write"].join(" "), // add/remove scopes as needed
    };
    const qs = new URLSearchParams(options).toString();
    return `${rootUrl}?${qs}`;
  }

  return (
    <div className="App">
      <p>
        Respond to tweets by searhing for keywords.
      </p>
      <TextInput />
      <a className="a-button row-container" href={getTwitterOauthUrl()}>
        <p>{" twitter auth"}</p>
      </a>
    </div>
  );
}

export default App;

