import React, {useEffect, useState} from 'react';
import * as constants from '../constants.js';

const SyncPairs = () => {
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
                {syncPairs.map((syncpair) => (
                    <div key={syncpair.id}>
                        <h1>Sync Pair: {syncpair.syncpair_name}</h1>
                        <h3>Trainer: {syncpair.trainer.name}</h3>
                        <p>{syncpair.trainer.description}</p>
                        {syncpair.pokemon[0].img_path && <img src={syncpair.pokemon[0].img_path}></img>}
                        <h3>Pokemon: {syncpair.pokemon[0].name}</h3>
                        <p>{syncpair.pokemon[0].description}</p>
                    </div>
                ))}
            </div>
        );
    }
}

SyncPairs.propTypes = {
};

export default SyncPairs;