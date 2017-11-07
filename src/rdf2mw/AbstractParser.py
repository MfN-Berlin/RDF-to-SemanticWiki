"""
Abstract base class for all parsers.

Created on 15.03.2016
@author: Alvaro.Ortiz
"""


class AbstractParser:
    """Abstract base class for all parsers."""

    def parse(self, path):
        """
        Parse an ontology.

        @param path:string path to a file
        @return SemanticModel: a object representing the parsed OWL
        @raise exception: if parsing failed.
        """
        raise NotImplementedError

    #
    # Static methods
    #

    # namespaces:
    # keys are short namespace prefixes,
    # values are fully expanded namespace URIs
    ns = {
        'base': "http://example.org/ontologies/test",
        'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        'owl': "http://www.w3.org/2002/07/owl#",
        'xml': "http://www.w3.org/XML/1998/namespace",
        'xsd': "http://www.w3.org/2001/XMLSchema#",
        'rdfs': "http://www.w3.org/2000/01/rdf-schema#"
    }

    @staticmethod
    def full(shortName, asURI=False):
        """
        Get the fully qualified name of a prefixed name.

        Expands the short prefix to the full version of the prefix.
        Returns either the curly braces version or the URIversion.
        Prefixes are in the dictionary ODMModel.ns

        e.g.: rdf:bla gets expanded to:
        * If asURI is True - {http://www.w3.org/1999/02/22-rdf-syntax-ns#}bla
        * If asURI is True - http://www.w3.org/1999/02/22-rdf-syntax-ns#bla

        If the namespace was not found in ODMModel.ns, then the shortName is returned.

        @shortName: string, name without the short version of the prefix
        @asURI: Boolean, when true, return the URI representation
        @return: string, the fully qualified name
        """
        prefix, rawName = shortName.split(':', 2)

        # expand with curly braces
        if asURI is False:
            if prefix in AbstractParser.ns:
                # get prefix from dictionary ODMModel.ns
                resp = "{" + AbstractParser.ns[prefix] + "}" + rawName
            else:
                # prefix not in dict, return shortName
                resp = shortName
        # expand as URI
        else:
            prefix = AbstractParser.ns[prefix].split('#', 2)[0]
            resp = prefix + "#" + rawName
        return resp

    @staticmethod
    def path(*args, **kwargs):
        """
        Join any number of qualified element names.

        example 2:
            ODMModel.path('owl:Class', 'rdfs:subClassOf'), startWith='descendant')
        returns:
            .//{http://www.w3.org/2002/07/owl#}Class/{http://www.w3.org/2000/01/rdf-schema#}subClassOf

        @param *args, string any number of qualified names in short form, e.g. rdf:bla
        @param kwargs, start the path with /, .// or //,
        resp. startWith=root(default)|descendant|any

        """
        expressions = {'root': '/', 'descendant': './/', 'any': '//'}
        exp = "/"
        if kwargs is not None:
            if 'startWith' in kwargs:
                exp = expressions[kwargs['startWith']]
        resp = ''
        for path in args:
            resp += exp + AbstractParser.full(path)
            exp = '/'
        return resp
