import React from 'react'

import { Query } from 'react-apollo'
import gql from 'graphql-tag'


class Tags extends React.Component{
    render(){
        const TAG_QUERY = gql`
          query{
              allTag{
                id
                    name
                    posts{
                    id
                    title
                    notes
                    }
              }
          }
        `
        return(
            <section>
                <Query query={TAG_QUERY}>
                    {({loading,error,data})=> {
                        if(loading) return <div>Loading</div>
                        if(error) return <div>error</div>
                        const TagLinks = data.allTag
                        return(
                            <div>
                                {TagLinks.map(tag => (
                                    <div>
                                        <h1>{tag.name}</h1>
                                        {
                                            tag.posts.map(post => (
                                                <div>
                                                    <h1>{post.name}</h1>
                                                    <p>{post.notes}</p>
                                                </div>
                                            ))
                                        }
                                    </div>
                                ))}
                            </div>
                        )
                    }}
                </Query>
            </section>
        )
    }
}
export default Tags