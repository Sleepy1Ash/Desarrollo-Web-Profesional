package edu.utvt.springdata;

import edu.utvt.springdata.data.entities.Address;
import edu.utvt.springdata.data.repositories.AddressRepository;
import edu.utvt.springdata.data.repositories.AuthorRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class OneToOneTests {
    @Autowired
    private AddressRepository addressRepository;
    @Autowired
    private AuthorRepository authorRepository;

    @Test
    void add(){
        Address address = new Address(null,"San Antonio", "Xonacatlan", this.authorRepository.findAll().getFirst());
        this.addressRepository.save(address);
    }

}
