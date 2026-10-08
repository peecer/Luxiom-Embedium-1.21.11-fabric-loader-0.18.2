package dev.peecer.luxiomport.luxium;

import net.fabricmc.api.ClientModInitializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * DEVELOPMENT-ONLY: This entrypoint intentionally does not port the old
 * renderer, shaders, optimizations, settings, or mixins.
 */
public final class LuxiumBootstrap implements ClientModInitializer {
    private static final Logger LOGGER = LoggerFactory.getLogger("luxium");

    @Override
    public void onInitializeClient() {
        LOGGER.warn("luxium 1.21.11 port bootstrap loaded. Original features are NOT implemented.");
    }
}
