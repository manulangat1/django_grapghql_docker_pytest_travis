import React from 'react'
import { Query  } from 'react-apollo'
import gql from 'graphql-tag'


class Post extends React.Component {
    
    render(){
        const POST_QUERY = gql`
            query{
                allPost{
                    id
                    name
                    notes
                }
            }
    `
        return(
            <section>
                <Query query={POST_QUERY}>
                   {({loading,error,data}) =>{
                       if (loading) return <div>Loading</div>
                       if (error) return <div>Error</div>
                       console.log(data)
                       const postLinks = data.allPost
                       return(
                           <div>
                               {
                                   postLinks.map(link => (
                                       <div>
                                           <h1>{link.name}</h1>
                                            <p>{link.notes}</p>
                                       </div>
                                   ))
                               }
                           </div>
                       )
                   }} 
                </Query>
            </section>

        )
    }
}
export default Post