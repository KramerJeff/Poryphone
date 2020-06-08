import React, {useEffect, useState} from 'react';

const SyncPairs = ({results}) => {
    const API_URL_BASE = 'api/v1';
    //const syncpairs = props.entries();
    const [syncPairs, setSyncPairs] = useState([]);
    let myArray = [];
    useEffect(() => {
        fetch(`${API_URL_BASE}/syncpairs`)
            .then(response => response.json())
            .then(
                (result) => {
                    setSyncPairs(Object.values(result));
                    myArray = Object.values(result);
                    console.log(`result: ` + result);
                    console.log(`Object.values(result): ${typeof (Object.values(result))}`);
                    console.log(Object.values(result));
                    console.log(`${typeof (syncPairs)}`);
                },
                (error) => {
                    console.error(`Something went horribly wrong ${error}`);
                }
            )
    }, []); 
    
    return (
        <div>
            <p>Hi Jeff!</p>
            {syncPairs.length > 0 ? <p>{syncPairs.length}</p> : <p>You really tried hehe</p>}
            {syncPairs.length > 0 ? syncPairs.map((syncPair, index) => {
                <div key={index}>
                    <p>{syncPair.id}</p>
                    <p>{syncPair.syncpair_name}</p>
                </div>
            }) : <p>You tried hehe</p>}
        </div>
    );
}

SyncPairs.propTypes = {
};

export default SyncPairs;