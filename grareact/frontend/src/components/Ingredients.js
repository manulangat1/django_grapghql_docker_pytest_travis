import React from 'react'

import { Query } from 'react-apollo'
import gql from 'graphql-tag'


class Ingredients extends React.Component{
    render(){
        const ING_QUERY = gql`
            query{
                allIngredients{
                    id
                    name
                }
            }
        `
        return(
            <section>
                <Query query= {ING_QUERY}>
                    {({loading,error,data}) => {
                        if (loading) return <div>Fetching</div>
                        if (error) return <div>Error</div>
                        console.log(data)
                        const IngLinks = data.allIngredients
                        return(
                            <div>
                                {
                                    IngLinks.map(link => (
                                        <div>
                                            <h1>{link.name}</h1>
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
export default Ingredients