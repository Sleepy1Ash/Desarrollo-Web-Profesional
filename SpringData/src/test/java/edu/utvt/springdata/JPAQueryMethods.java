package edu.utvt.springdata;

import edu.utvt.springdata.data.entities.Player;
import edu.utvt.springdata.data.repositories.PlayerRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.PageRequest;

@SpringBootTest
public class JPAQueryMethods {

    @Autowired
    private PlayerRepository playerRepository;
    @Test
    void findByFullName(){
        String fullName="Harrison Ingram";
        playerRepository.findByFullName(fullName).forEach(System.out::println);
    }

    @Test
    void findByFullNameContaining(){
        String Name="Harrison";
        this.playerRepository.findByFullNameContaining(Name).forEach(System.out::println);
    }

    @Test
    void findByTeamAndAge(){
        String team="Uta";
        Integer age=21;
        this.playerRepository.findByTeamAndAge(team,age).forEach(System.out::println);
    }

    @Test
    void findByTeamAndPeageble(){
        Pageable pageable= PageRequest.of(0,10);
        Page<Player> page= this.playerRepository.findByTeam("Cha",pageable);
        System.out.println(page.getTotalElements());
        System.out.println(page.getTotalPages());
    }
}
