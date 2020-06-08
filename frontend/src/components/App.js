import React, {useEffect, useState} from 'react';
import {render} from 'react-dom';

const API_URL_BASE = 'poryphone.com/api/v1';

const App = () => {
    const [syncPairs, setSyncPairs] = useState({});

    useEffect(() => {
        fetch(`http://${API_URL_BASE}/syncpairs`)
        .then(response => response.json)
        .then(
            (result) => {
                setSyncPairs(result);
            },
            (error) => {
                console.error(`Something went horribly wrong ${error}`);
            }
        )
    }, [syncPairs]);

    return ( 
        <div>
            
        </div>
    );
}