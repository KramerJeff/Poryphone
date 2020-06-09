import React, {useEffect, useState} from 'react';

const SyncPairs = ({results}) => {
    const API_URL_BASE = 'http://localhost:8000/api/v1';
    const [error, setError] = useState(null);
    const [syncPairs, setSyncPairs] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    useEffect(() => {
        fetch(`${API_URL_BASE}/syncpairs`)
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
                    <div>
                        <h1 key={item.id}>Sync Pair: {item.syncpair_name}</h1>
                        <h3 key={item.id}>Trainer: {item.trainer.name}</h3>
                        <p key={item.id}>{item.trainer.description}</p>
                        <h3 key={item.id}>Pokemon: {item.pokemon.name}</h3>
                        <p key={item.id}>{item.pokemon.description}</p>
                    </div>
                ))}
            </div>
        );
    }
}

SyncPairs.propTypes = {
};

export default SyncPairs;