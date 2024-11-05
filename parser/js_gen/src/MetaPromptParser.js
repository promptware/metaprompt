// Generated from src/MetaPrompt.g4 by ANTLR 4.13.2
// jshint ignore: start
import antlr4 from 'antlr4';
import MetaPromptListener from './MetaPromptListener.js';
import MetaPromptVisitor from './MetaPromptVisitor.js';

const serializedATN = [4,1,10,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,
2,5,7,5,1,0,1,0,1,0,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,2,4,2,23,8,2,11,2,
12,2,24,1,2,3,2,28,8,2,4,2,30,8,2,11,2,12,2,31,1,3,1,3,1,3,1,3,1,4,1,4,1,
4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,50,8,4,1,5,4,5,53,8,5,11,5,12,
5,54,1,5,1,24,0,6,0,2,4,6,8,10,0,0,56,0,12,1,0,0,0,2,18,1,0,0,0,4,29,1,0,
0,0,6,33,1,0,0,0,8,49,1,0,0,0,10,52,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,
14,1,1,0,0,0,15,17,3,4,2,0,16,15,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,
19,1,0,0,0,19,3,1,0,0,0,20,18,1,0,0,0,21,23,3,10,5,0,22,21,1,0,0,0,23,24,
1,0,0,0,24,25,1,0,0,0,24,22,1,0,0,0,25,27,1,0,0,0,26,28,3,6,3,0,27,26,1,
0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,22,1,0,0,0,30,31,1,0,0,0,31,29,1,0,
0,0,31,32,1,0,0,0,32,5,1,0,0,0,33,34,5,1,0,0,34,35,3,8,4,0,35,36,5,2,0,0,
36,7,1,0,0,0,37,38,5,4,0,0,38,39,3,2,1,0,39,40,5,5,0,0,40,41,3,2,1,0,41,
42,5,6,0,0,42,43,3,2,1,0,43,50,1,0,0,0,44,45,5,4,0,0,45,46,3,2,1,0,46,47,
5,5,0,0,47,48,3,2,1,0,48,50,1,0,0,0,49,37,1,0,0,0,49,44,1,0,0,0,50,9,1,0,
0,0,51,53,5,3,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,
0,55,11,1,0,0,0,6,18,24,27,31,49,54];


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.atn.PredictionContextCache();

export default class MetaPromptParser extends antlr4.Parser {

    static grammarFileName = "MetaPrompt.g4";
    static literalNames = [ null, "'['", "']'", null, "':if'", "':then'", 
                            "':else'" ];
    static symbolicNames = [ null, null, null, "CHAR", "IF_KW", "THEN_KW", 
                             "ELSE_KW", "ESCAPED_CHAR", "ESCAPE", "SPECIAL_CHAR", 
                             "ESCAPE_CHAR" ];
    static ruleNames = [ "prompt", "exprs", "expr", "meta", "meta_body", 
                         "text" ];

    constructor(input) {
        super(input);
        this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
        this.ruleNames = MetaPromptParser.ruleNames;
        this.literalNames = MetaPromptParser.literalNames;
        this.symbolicNames = MetaPromptParser.symbolicNames;
    }



	prompt() {
	    let localctx = new PromptContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 0, MetaPromptParser.RULE_prompt);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 12;
	        this.exprs();
	        this.state = 13;
	        this.match(MetaPromptParser.EOF);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	exprs() {
	    let localctx = new ExprsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 2, MetaPromptParser.RULE_exprs);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 18;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===3) {
	            this.state = 15;
	            this.expr();
	            this.state = 20;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	expr() {
	    let localctx = new ExprContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 4, MetaPromptParser.RULE_expr);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 29; 
	        this._errHandler.sync(this);
	        var _alt = 1;
	        do {
	        	switch (_alt) {
	        	case 1:
	        		this.state = 22; 
	        		this._errHandler.sync(this);
	        		var _alt = 1+1;
	        		do {
	        			switch (_alt) {
	        			case 1+1:
	        				this.state = 21;
	        				this.text();
	        				break;
	        			default:
	        				throw new antlr4.error.NoViableAltException(this);
	        			}
	        			this.state = 24; 
	        			this._errHandler.sync(this);
	        			_alt = this._interp.adaptivePredict(this._input,1, this._ctx);
	        		} while ( _alt!=1 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER );
	        		this.state = 27;
	        		this._errHandler.sync(this);
	        		_la = this._input.LA(1);
	        		if(_la===1) {
	        		    this.state = 26;
	        		    this.meta();
	        		}

	        		break;
	        	default:
	        		throw new antlr4.error.NoViableAltException(this);
	        	}
	        	this.state = 31; 
	        	this._errHandler.sync(this);
	        	_alt = this._interp.adaptivePredict(this._input,3, this._ctx);
	        } while ( _alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER );
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	meta() {
	    let localctx = new MetaContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 6, MetaPromptParser.RULE_meta);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 33;
	        this.match(MetaPromptParser.T__0);
	        this.state = 34;
	        this.meta_body();
	        this.state = 35;
	        this.match(MetaPromptParser.T__1);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	meta_body() {
	    let localctx = new Meta_bodyContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 8, MetaPromptParser.RULE_meta_body);
	    try {
	        this.state = 49;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,4,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 37;
	            this.match(MetaPromptParser.IF_KW);
	            this.state = 38;
	            this.exprs();
	            this.state = 39;
	            this.match(MetaPromptParser.THEN_KW);
	            this.state = 40;
	            this.exprs();
	            this.state = 41;
	            this.match(MetaPromptParser.ELSE_KW);
	            this.state = 42;
	            this.exprs();
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 44;
	            this.match(MetaPromptParser.IF_KW);
	            this.state = 45;
	            this.exprs();
	            this.state = 46;
	            this.match(MetaPromptParser.THEN_KW);
	            this.state = 47;
	            this.exprs();
	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	text() {
	    let localctx = new TextContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 10, MetaPromptParser.RULE_text);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 52; 
	        this._errHandler.sync(this);
	        var _alt = 1;
	        do {
	        	switch (_alt) {
	        	case 1:
	        		this.state = 51;
	        		this.match(MetaPromptParser.CHAR);
	        		break;
	        	default:
	        		throw new antlr4.error.NoViableAltException(this);
	        	}
	        	this.state = 54; 
	        	this._errHandler.sync(this);
	        	_alt = this._interp.adaptivePredict(this._input,5, this._ctx);
	        } while ( _alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER );
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


}

MetaPromptParser.EOF = antlr4.Token.EOF;
MetaPromptParser.T__0 = 1;
MetaPromptParser.T__1 = 2;
MetaPromptParser.CHAR = 3;
MetaPromptParser.IF_KW = 4;
MetaPromptParser.THEN_KW = 5;
MetaPromptParser.ELSE_KW = 6;
MetaPromptParser.ESCAPED_CHAR = 7;
MetaPromptParser.ESCAPE = 8;
MetaPromptParser.SPECIAL_CHAR = 9;
MetaPromptParser.ESCAPE_CHAR = 10;

MetaPromptParser.RULE_prompt = 0;
MetaPromptParser.RULE_exprs = 1;
MetaPromptParser.RULE_expr = 2;
MetaPromptParser.RULE_meta = 3;
MetaPromptParser.RULE_meta_body = 4;
MetaPromptParser.RULE_text = 5;

class PromptContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = MetaPromptParser.RULE_prompt;
    }

	exprs() {
	    return this.getTypedRuleContext(ExprsContext,0);
	};

	EOF() {
	    return this.getToken(MetaPromptParser.EOF, 0);
	};

	enterRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.enterPrompt(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.exitPrompt(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof MetaPromptVisitor ) {
	        return visitor.visitPrompt(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class ExprsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = MetaPromptParser.RULE_exprs;
    }

	expr = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExprContext);
	    } else {
	        return this.getTypedRuleContext(ExprContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.enterExprs(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.exitExprs(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof MetaPromptVisitor ) {
	        return visitor.visitExprs(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class ExprContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = MetaPromptParser.RULE_expr;
    }

	text = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(TextContext);
	    } else {
	        return this.getTypedRuleContext(TextContext,i);
	    }
	};

	meta = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(MetaContext);
	    } else {
	        return this.getTypedRuleContext(MetaContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.enterExpr(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.exitExpr(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof MetaPromptVisitor ) {
	        return visitor.visitExpr(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class MetaContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = MetaPromptParser.RULE_meta;
    }

	meta_body() {
	    return this.getTypedRuleContext(Meta_bodyContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.enterMeta(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.exitMeta(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof MetaPromptVisitor ) {
	        return visitor.visitMeta(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class Meta_bodyContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = MetaPromptParser.RULE_meta_body;
    }

	IF_KW() {
	    return this.getToken(MetaPromptParser.IF_KW, 0);
	};

	exprs = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExprsContext);
	    } else {
	        return this.getTypedRuleContext(ExprsContext,i);
	    }
	};

	THEN_KW() {
	    return this.getToken(MetaPromptParser.THEN_KW, 0);
	};

	ELSE_KW() {
	    return this.getToken(MetaPromptParser.ELSE_KW, 0);
	};

	enterRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.enterMeta_body(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.exitMeta_body(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof MetaPromptVisitor ) {
	        return visitor.visitMeta_body(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class TextContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = MetaPromptParser.RULE_text;
    }

	CHAR = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(MetaPromptParser.CHAR);
	    } else {
	        return this.getToken(MetaPromptParser.CHAR, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.enterText(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof MetaPromptListener ) {
	        listener.exitText(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof MetaPromptVisitor ) {
	        return visitor.visitText(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}




MetaPromptParser.PromptContext = PromptContext; 
MetaPromptParser.ExprsContext = ExprsContext; 
MetaPromptParser.ExprContext = ExprContext; 
MetaPromptParser.MetaContext = MetaContext; 
MetaPromptParser.Meta_bodyContext = Meta_bodyContext; 
MetaPromptParser.TextContext = TextContext; 
