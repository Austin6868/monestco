import React from 'react'; 
import '../styles/Comparison.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
import companies from '../data/companies.json';
import { CSSTransition } from 'react-transition-group';

var filterBy = [
    'Clothing', 'Sportswear', 'Shoes', 'All'
];

class CompareSearch extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            unisex: false,
            women: false,
            sportswear: false,
            shoes: false,
            luxury: false,
            all: false,
            foundCompanies: [],
            changehandled: false
        };  
        this.toggleClassUnisex = this.toggleClassUnisex.bind(this);
        this.toggleClassWomen = this.toggleClassWomen.bind(this);
        this.toggleClassSportswear = this.toggleClassSportswear.bind(this);
        this.toggleClassShoes = this.toggleClassShoes.bind(this);
        this.toggleClassLuxury = this.toggleClassLuxury.bind(this);
        this.toggleClassAll = this.toggleClassAll.bind(this);
        this.handleChange = this.handleChange.bind(this);
    };

    toggleClassUnisex() {
        const currentState = this.state.unisex;
        this.setState({unisex: !currentState});
    }
    toggleClassWomen() {
        const currentState = this.state.women;
        this.setState({women: !currentState});
    }
    toggleClassSportswear() {
        const currentState = this.state.sportswear;
        this.setState({sportswear: !currentState});
    }
    toggleClassShoes() {
        const currentState = this.state.shoes;
        this.setState({shoes: !currentState});
    }
    toggleClassLuxury() {
        const currentState = this.state.luxury;
        this.setState({luxury: !currentState});
    }
    toggleClassAll() {
        const currentState = !this.state.all;
        this.setState({all: !currentState});
    }

    handleChange() {
        console.log("handlechange");
        var search = document.getElementById("categorysearch").value.toLowerCase();
        const comps = this.mapCompanies(companies);
        const foundCompanies = comps.filter(comp => {
            return comp.toLowerCase().match(search);
        })
        this.setState({ 
            foundCompanies: foundCompanies,
            changehandled: true
        });      
    }

    mapCompanies = (companies) => {
        console.log("mapcompanies");
        return companies.companies.map(company => {
            return company.name;
        })
    }

    renderCompanies = (companies) => {
        console.log("rendercompanies");
        return companies.map((company, i) => {
            return <CSSTransition timeout={300}>
                        <div key={i} className={this.state.changehandled ? 'rendercompanies' : null}>
                            {company}
                        </div>  
                    </CSSTransition>              
        })
    }

    render() {   
        return (
            <div style={{display:'flex', flexDirection:'column'}}>
                <p style={{margin: '0 0 20px 0', fontSize: '18px', lineHeight:'34px', color: '#3D3E3F'}}>Filter by:</p>
                <div style={{display:'flex', flexWrap:'wrap', marginBottom:'10px'}}>
                <span id="filterbutton"
                    className={this.state.unisex ? 'categoryfocus' : null}
                    onClick = {this.toggleClassUnisex}
                >Unisex</span>
                <span id="filterbutton1"
                    className={this.state.women ? 'categoryfocus' : null}
                    onClick = {this.toggleClassWomen}
                >Women</span>
                <span id="filterbutton2"
                    className={this.state.sportswear ? 'categoryfocus' : null}
                    onClick = {this.toggleClassSportswear}
                >Sportswear</span>
                <div style={{marginTop: '10%'}}></div>
                <span id="filterbutton3"
                    className={this.state.shoes ? 'categoryfocus' : null}
                    onClick = {this.toggleClassShoes}
                >Shoes & Accessories</span>
                <span id="filterbutton4"
                    className={this.state.luxury ? 'categoryfocus' : null}
                    onClick = {this.toggleClassLuxury}
                >Luxury</span>
                <span id="filterbutton5"
                    className={this.state.all ? 'categoryfocus' : null}
                    onClick = {this.toggleClassAll}
                >All</span>
                </div>
                <div className='horizontal-row'/>
                {/* <hr style={{width: '100%'}}/> */}
                <div style={{position:'relative'}}>
                <FontAwesomeIcon style={{position: "absolute", marginTop: '9px', marginLeft: '5px', color: 'rgba(50, 50, 50, 0.5'}} icon={faSearch} />
                <input type="text" id="categorysearch" onChange={this.handleChange} placeholder="Search the brand" style={{width: '85%', height: '34px', border:'2px solid #BDBDBD'}} />
                </div>
                <div style={{marginTop:'20px'}}>
                    {this.renderCompanies(this.state.foundCompanies)}
                </div>
            </div>
            )
        }
}

export default CompareSearch;
