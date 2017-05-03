class Laptop(object):

    def __init__(self, blob):
        blob = blob.split('\n')
        self.name = blob[0]
        self.details = None
        self.cost = None
        self.offers = None
        if len(blob) >= 11:
            self.details = blob[1:10]
            self.cost = blob[10]
            self.offers = blob[11:]
        
    def __repr__(self):
        return 'Laptop({0}, {1}, {2}, {3})'.format(self.name, self.details, self.cost, self.offers)

    def __str__(self):
        name, details, cost, offers = self.name, self.details, self.cost, self.offers

        pretty_str = ['Name : {}'.format(name)]
        
        details_header = 'Details :\n'
        details_body = '\n'.join(['{}. {}'.format(i+1, detail) for i, detail in enumerate(details)])
        details_str = details_header + details_body 
        pretty_str.append(details_str)
        
        pretty_str.append('Cost : {}'.format(cost))
        
        if offers is not None:
            offers_header = 'Offers :\n'
            offers_body = '\n'.join(['{}. {}'.format(i+1, offer) for i, offer in enumerate(offers)])
            offers_str = offers_header + offers_body 
            pretty_str.append(offers_str)

        return '\n'.join(pretty_str)
