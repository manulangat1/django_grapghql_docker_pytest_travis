import React from 'react';
import logo from './logo.svg';
import './App.css';
import LinkList from './components/LinkList'
import Post from './components/Post'
import PostDetail from './components/PostDetail'
import Tags from './components/Tags'
import Ingredients from './components/Ingredients'
import { ApolloProvider } from 'react-apollo'
import { ApolloClient } from 'apollo-client'
import { createHttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'


// 2
const httpLink = createHttpLink({
  uri: 'http://127.0.0.1:8000/graphql'
})

// 3
const client = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache()
})
function App() {
  return (
    <div className="App">
      <ApolloProvider client={client}>
    <section>
      <LinkList />
      <Ingredients />
      <h1>Post</h1>
      <Post />
      <hr></hr>
      <Tags />
      <hr></hr>
      <PostDetail />
    </section>
    </ApolloProvider>
    </div>
  );
}

export default App;
