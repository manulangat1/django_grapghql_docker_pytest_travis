import React from 'react'
import { Query  } from 'react-apollo'
import gql from 'graphql-tag'


class Post extends React.Component {
    
    render(){
        const POST_QUERY = gql`
            query{
                allPost{
                    id
                    title
                    tag{
                               id
                               name
                             }
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
                                           <h1>{link.title}</h1>
                                            <p>{link.notes}</p>
                                            { link.tag.map(t => (
                                                <div>
                                                    <h1>{t.name}</h1>
                                                </div>
                                            ))}
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