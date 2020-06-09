import React, {useEffect, useState} from 'react';

const SyncPairs = ({results}) => {
    const API_URL_BASE = 'https://poryhone.herokuapp.com/api/v1';
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
        return (<p>loading....</p>);
    }
    else {
        return (
            <div>
                {<p>{syncPairs.length}</p>}
                <ul>
                    {syncPairs.map((syncPair, index) => {
                        //let values = Object.values(syncPair);
                        {<li key={index}>{syncPair.syncpair_name}</li>}
                        /* {<li key={index}>{values[0]}</li>} */
                    })}
                </ul>
            </div>
        );
    }
}

SyncPairs.propTypes = {
};

export default SyncPairs;