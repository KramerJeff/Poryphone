import React from 'react';
import {render} from 'react-dom';
import SyncPairs from './SyncPairs';


const App = () => {
    return ( 
        <div>
           <SyncPairs/>
        </div>
    );
}

export default App;
const container = document.getElementById('app');
render(<App/>, container);