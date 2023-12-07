# Place your imports here


class RSA(object):
    """
    RSA Encryption/Decryption Algorithm

    Parameters:
    p, q        : int       prime numbers
    n           : int       modulus for public&private key
    phi         : int       lambda(n)
    e           : int       public key
    d           : int       private key

    Method:
    compute_key  : int, int -> None     compute public private key from p, q
    encrypt     : int -> int            encrypte msg
    decrypt     : int -> int            decrypt cipher text
    """
    p: int
    q: int
    n: int
    phi: int
    e: int
    d: int

    def encrypt(self, msg: int) -> int:
        """Enrypt the message"""
        # TODO: Implement me
        return pow(msg, self.e) % self.n

    def decrypt(self, cipher_text: int) -> int:
        """Decrypt the cipher text"""
        # TODO: Implement me
        return pow(cipher_text, self.d) % self.n 

    def compute_key(self, p: int, q: int, coprime_index: int = 0) -> int:
        """
        Compute Public&Private Key and assign them to class attribute

        Compute nth coprime according to the coprime index (default to 0)
        """
        # TODO: Implement me
        
        self.p = p

        self.q = q

        self.n = p*q

        self.phi = (p-1)*(q-1)

        all_coprimes_of_phi = []
        for i in range (2, self.phi):
            if(self.find_gcd(self.phi, i) == 1):
                all_coprimes_of_phi.append(i)

        #assuming coprime_index is always passed and it's 1 based
        self.e = all_coprimes_of_phi[coprime_index-1]

        #find d (using brute force)
        self.d = self.find_d(self.e, self.phi)




    def find_gcd(self, p, q):
        gcd = 1
        for i in range(1,max(p,q)):
            if(p%i==0 and q%i==0):
                gcd = i
        return gcd


    def find_d(self, e, phi):

        for i in range(1, phi):
            if (i*e)%phi == 1:
                return i

        return -1




