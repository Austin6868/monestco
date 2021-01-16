import logo from './DP.png';
import NavigationBar from './components/navigationbar/navigationbar';
import './App.css';
import { BrowserRouter as Router } from 'react-router-dom';
function App() {
  return (
    <Router>
      <NavigationBar />
    </Router>
  );
}

export default App;
