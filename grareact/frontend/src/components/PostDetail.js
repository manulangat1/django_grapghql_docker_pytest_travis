import React from 'react'

import { Query } from 'react-apollo'
import gql from 'graphql-tag'

class PostDetail extends React.Component{
    render(){
        const POST_D_QUERY = gql`
        query {
            category(id: 2) {
              name
              ingredients{
                id
                name
              }
            }
        }
        `
        return(
            <section>
                <Query query={POST_D_QUERY}>
                    {({loading,error,data}) => {
                        if (loading) return <div>Loading</div>
                        if (error) return <div>error</div>
                        
                        const postD = data.category
                        console.log(postD)
                        return(
                            
                                    <div>
                                        <h1>{postD && postD.name}</h1>
                                        {postD.ingredients.map(ing => (
                                            <div>
                                                <h1>{ing.name}</h1>
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
export default PostDetail