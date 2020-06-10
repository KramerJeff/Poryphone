import React, {useEffect, useState} from 'react';
import * as constants from '../constants.js';

const SyncPairs = ({results}) => {
    const [error, setError] = useState(null);
    const [syncPairs, setSyncPairs] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    useEffect(() => {
        fetch(`${constants.API_URL_BASE}/syncpairs`)
            .then(response => response.json())
            .then(
                (result) => {
                    setIsLoaded(true);
                    setSyncPairs(result);
                    console.log('useEffect ' + result);
                },
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
    }, []); 

    if(error) {
        return(<p>Error: {error.message}</p>);
    }
    else if(!isLoaded) {
        return (<p>Loading....</p>);
    }
    else {
        return (
            <div>
                {syncPairs.map((item) => (
                    <div key={item.id}>
                        <h1>Sync Pair: {item.syncpair_name}</h1>
                        <h3>Trainer: {item.trainer.name}</h3>
                        <p>{item.trainer.description}</p>
                        <h3>Pokemon: {item.pokemon[0].name}</h3>
                        <p>{item.pokemon[0].description}</p>
                    </div>
                ))}
            </div>
        );
    }
}

SyncPairs.propTypes = {
};

export default SyncPairs;